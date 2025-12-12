"""Failed download tracking for retry capability."""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

from infrastructure.core.exceptions import FileOperationError
from infrastructure.core.logging_utils import get_logger
from infrastructure.literature.core.core import DownloadResult
from infrastructure.literature.core.config import LiteratureConfig

logger = get_logger(__name__)


class FailedDownloadTracker:
    """Tracks failed PDF downloads for retry capability.
    
    Maintains a JSON file with failed download attempts, including
    metadata needed for retry operations. Supports filtering by
    retriable status (network errors, timeouts).
    """
    
    def __init__(self, config: LiteratureConfig):
        """Initialize failed download tracker.
        
        Args:
            config: Literature configuration.
        """
        self.config = config
        self.tracker_path = Path(config.download_dir).parent / "failed_downloads.json"
        self._failures: Dict[str, Dict[str, Any]] = {}
        self._load_tracker()
    
    def _load_tracker(self) -> None:
        """Load failed downloads from disk if tracker exists."""
        if self.tracker_path.exists():
            try:
                with open(self.tracker_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self._failures = data.get("failures", {})
                logger.debug(f"Loaded {len(self._failures)} failed downloads from tracker")
            except (json.JSONDecodeError, KeyError, OSError) as e:
                logger.warning(f"Failed to load failed downloads tracker: {e}")
                self._failures = {}
    
    def _save_tracker(self) -> None:
        """Save failed downloads to disk."""
        try:
            # Ensure directory exists
            self.tracker_path.parent.mkdir(parents=True, exist_ok=True)
            
            data = {
                "version": "1.0",
                "updated": datetime.now().isoformat(),
                "failures": self._failures
            }
            
            # Write atomically (write to temp, then rename)
            temp_path = self.tracker_path.with_suffix('.tmp')
            with open(temp_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            temp_path.replace(self.tracker_path)
            
            logger.debug(f"Saved {len(self._failures)} failed downloads to tracker")
        except OSError as e:
            raise FileOperationError(
                f"Failed to save failed downloads tracker: {e}",
                context={"path": str(self.tracker_path)}
            )
    
    def save_failed(
        self,
        citation_key: str,
        download_result: DownloadResult,
        title: Optional[str] = None,
        source: Optional[str] = None
    ) -> None:
        """Save a failed download to the tracker.
        
        Args:
            citation_key: Citation key for the paper.
            download_result: DownloadResult with failure information.
            title: Optional paper title.
            source: Optional source database.
        """
        if download_result.success:
            # Don't track successful downloads
            return
        
        # Get title and source from result if not provided
        if not title and download_result.result:
            title = download_result.result.title
        if not source and download_result.result:
            source = download_result.result.source or "unknown"
        
        failure_data = {
            "citation_key": citation_key,
            "title": title or "Unknown",
            "failure_reason": download_result.failure_reason or "unknown",
            "failure_message": download_result.failure_message or "No error message",
            "attempted_urls": download_result.attempted_urls or [],
            "source": source or "unknown",
            "timestamp": datetime.now().isoformat(),
            "retriable": download_result.is_retriable
        }
        
        self._failures[citation_key] = failure_data
        self._save_tracker()
        logger.debug(f"Tracked failed download: {citation_key} ({download_result.failure_reason})")
    
    def load_failed(self) -> Dict[str, Dict[str, Any]]:
        """Load all failed downloads.
        
        Returns:
            Dictionary mapping citation_key to failure data.
        """
        return self._failures.copy()
    
    def get_retriable_failed(self) -> Dict[str, Dict[str, Any]]:
        """Get only retriable failed downloads.
        
        Returns:
            Dictionary of retriable failures (network_error, timeout).
        """
        return {
            key: data
            for key, data in self._failures.items()
            if data.get("retriable", False)
        }
    
    def clear_failed(self, citation_keys: Optional[List[str]] = None) -> None:
        """Clear failed downloads from tracker.
        
        Args:
            citation_keys: Optional list of citation keys to clear.
                          If None, clears all failures.
        """
        if citation_keys is None:
            self._failures = {}
        else:
            for key in citation_keys:
                self._failures.pop(key, None)
        
        self._save_tracker()
        logger.debug(f"Cleared {len(citation_keys) if citation_keys else 'all'} failed downloads")
    
    def remove_successful(self, citation_key: str) -> None:
        """Remove a citation key from failed tracker (download succeeded).
        
        Args:
            citation_key: Citation key that successfully downloaded.
        """
        if citation_key in self._failures:
            del self._failures[citation_key]
            self._save_tracker()
            logger.debug(f"Removed successful download from tracker: {citation_key}")
    
    def is_failed(self, citation_key: str) -> bool:
        """Check if a citation key has a failed download.
        
        Args:
            citation_key: Citation key to check.
        
        Returns:
            True if the citation key has a tracked failure.
        """
        return citation_key in self._failures
    
    def has_failures(self) -> bool:
        """Check if tracker has any failed downloads.
        
        Returns:
            True if any failures are tracked.
        """
        return len(self._failures) > 0
    
    def count_failures(self) -> int:
        """Get count of failed downloads.
        
        Returns:
            Number of failed downloads tracked.
        """
        return len(self._failures)
    
    def count_retriable(self) -> int:
        """Get count of retriable failed downloads.
        
        Returns:
            Number of retriable failures.
        """
        return len(self.get_retriable_failed())

