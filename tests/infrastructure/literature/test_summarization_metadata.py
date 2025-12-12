#!/usr/bin/env python3
"""Tests for summary metadata management.

Tests SummaryMetadata dataclass and SummaryMetadataManager with real file operations.
No mocks - tests actual component behavior.
"""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from infrastructure.literature.summarization.metadata import (
    SummaryMetadata,
    SummaryMetadataManager,
)
from infrastructure.core.exceptions import FileOperationError


class TestSummaryMetadata:
    """Test SummaryMetadata dataclass."""
    
    def test_metadata_creation(self):
        """Test creating summary metadata."""
        metadata = SummaryMetadata(
            citation_key="test2024paper",
            input_words=1000,
            input_chars=5000,
            output_words=200,
            compression_ratio=0.2,
            generation_time=30.0,
            words_per_second=6.67,
            quality_score=0.9,
            validation_errors=[],
            attempts=1,
            generated="2024-01-01T00:00:00",
            pdf_path="data/pdfs/test2024paper.pdf",
            pdf_size_bytes=100000,
            truncated=False
        )
        
        assert metadata.citation_key == "test2024paper"
        assert metadata.input_words == 1000
        assert metadata.output_words == 200
        assert metadata.compression_ratio == 0.2
        assert metadata.quality_score == 0.9
        assert metadata.attempts == 1
        assert metadata.pdf_path == "data/pdfs/test2024paper.pdf"
        assert metadata.truncated is False
    
    def test_metadata_defaults(self):
        """Test metadata with default values."""
        metadata = SummaryMetadata(
            citation_key="test2024paper",
            input_words=1000,
            input_chars=5000,
            output_words=200,
            compression_ratio=0.2,
            generation_time=30.0,
            words_per_second=6.67,
            quality_score=0.9,
            validation_errors=[],
            attempts=1,
            generated="2024-01-01T00:00:00"
        )
        
        assert metadata.pdf_path is None
        assert metadata.pdf_size_bytes is None
        assert metadata.truncated is False
        assert metadata.reference_count is None
    
    def test_metadata_to_dict(self):
        """Test converting metadata to dictionary."""
        metadata = SummaryMetadata(
            citation_key="test2024paper",
            input_words=1000,
            input_chars=5000,
            output_words=200,
            compression_ratio=0.2,
            generation_time=30.0,
            words_per_second=6.67,
            quality_score=0.9,
            validation_errors=["minor issue"],
            attempts=1,
            generated="2024-01-01T00:00:00"
        )
        
        data = metadata.to_dict()
        
        assert isinstance(data, dict)
        assert data["citation_key"] == "test2024paper"
        assert data["input_words"] == 1000
        assert data["output_words"] == 200
        assert data["validation_errors"] == ["minor issue"]


class TestSummaryMetadataManager:
    """Test SummaryMetadataManager class."""
    
    def test_manager_initialization_new_file(self, tmp_path):
        """Test initializing manager with non-existent file."""
        metadata_path = tmp_path / "metadata.json"
        manager = SummaryMetadataManager(metadata_path)
        
        assert manager.metadata_path == metadata_path
        assert len(manager.get_all_metadata()) == 0
    
    def test_manager_initialization_existing_file(self, tmp_path):
        """Test initializing manager with existing file."""
        metadata_path = tmp_path / "metadata.json"
        
        # Create existing metadata file
        existing_data = {
            "test2024paper": {
                "citation_key": "test2024paper",
                "input_words": 1000,
                "input_chars": 5000,
                "output_words": 200,
                "compression_ratio": 0.2,
                "generation_time": 30.0,
                "words_per_second": 6.67,
                "quality_score": 0.9,
                "validation_errors": [],
                "attempts": 1,
                "generated": "2024-01-01T00:00:00"
            }
        }
        
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f)
        
        manager = SummaryMetadataManager(metadata_path)
        
        assert len(manager.get_all_metadata()) == 1
        metadata = manager.get_metadata("test2024paper")
        assert metadata is not None
        assert metadata.citation_key == "test2024paper"
        assert metadata.input_words == 1000
    
    def test_manager_initialization_invalid_json(self, tmp_path):
        """Test initializing manager with invalid JSON file."""
        metadata_path = tmp_path / "metadata.json"
        
        # Create invalid JSON file
        with open(metadata_path, 'w', encoding='utf-8') as f:
            f.write("invalid json content {")
        
        manager = SummaryMetadataManager(metadata_path)
        
        # Should handle gracefully and start with empty metadata
        assert len(manager.get_all_metadata()) == 0
    
    def test_add_metadata(self, tmp_path):
        """Test adding metadata."""
        metadata_path = tmp_path / "metadata.json"
        manager = SummaryMetadataManager(metadata_path)
        
        metadata = SummaryMetadata(
            citation_key="test2024paper",
            input_words=1000,
            input_chars=5000,
            output_words=200,
            compression_ratio=0.2,
            generation_time=30.0,
            words_per_second=6.67,
            quality_score=0.9,
            validation_errors=[],
            attempts=1,
            generated="2024-01-01T00:00:00"
        )
        
        manager.add_metadata(metadata)
        
        # Verify it was saved to file
        assert metadata_path.exists()
        with open(metadata_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            assert "test2024paper" in data
        
        # Verify it can be retrieved
        retrieved = manager.get_metadata("test2024paper")
        assert retrieved is not None
        assert retrieved.citation_key == "test2024paper"
        assert retrieved.input_words == 1000
    
    def test_update_metadata(self, tmp_path):
        """Test updating existing metadata."""
        metadata_path = tmp_path / "metadata.json"
        manager = SummaryMetadataManager(metadata_path)
        
        # Add initial metadata
        metadata1 = SummaryMetadata(
            citation_key="test2024paper",
            input_words=1000,
            input_chars=5000,
            output_words=200,
            compression_ratio=0.2,
            generation_time=30.0,
            words_per_second=6.67,
            quality_score=0.9,
            validation_errors=[],
            attempts=1,
            generated="2024-01-01T00:00:00"
        )
        manager.add_metadata(metadata1)
        
        # Update with new metadata
        metadata2 = SummaryMetadata(
            citation_key="test2024paper",
            input_words=1200,
            input_chars=6000,
            output_words=250,
            compression_ratio=0.208,
            generation_time=35.0,
            words_per_second=7.14,
            quality_score=0.95,
            validation_errors=[],
            attempts=1,
            generated="2024-01-02T00:00:00"
        )
        manager.add_metadata(metadata2)
        
        # Verify update
        retrieved = manager.get_metadata("test2024paper")
        assert retrieved is not None
        assert retrieved.input_words == 1200
        assert retrieved.quality_score == 0.95
    
    def test_get_metadata_existing(self, tmp_path):
        """Test getting existing metadata."""
        metadata_path = tmp_path / "metadata.json"
        manager = SummaryMetadataManager(metadata_path)
        
        metadata = SummaryMetadata(
            citation_key="test2024paper",
            input_words=1000,
            input_chars=5000,
            output_words=200,
            compression_ratio=0.2,
            generation_time=30.0,
            words_per_second=6.67,
            quality_score=0.9,
            validation_errors=[],
            attempts=1,
            generated="2024-01-01T00:00:00"
        )
        manager.add_metadata(metadata)
        
        retrieved = manager.get_metadata("test2024paper")
        assert retrieved is not None
        assert retrieved.citation_key == "test2024paper"
    
    def test_get_metadata_nonexistent(self, tmp_path):
        """Test getting non-existent metadata."""
        metadata_path = tmp_path / "metadata.json"
        manager = SummaryMetadataManager(metadata_path)
        
        retrieved = manager.get_metadata("nonexistent")
        assert retrieved is None
    
    def test_get_all_metadata(self, tmp_path):
        """Test getting all metadata."""
        metadata_path = tmp_path / "metadata.json"
        manager = SummaryMetadataManager(metadata_path)
        
        # Add multiple metadata entries
        for i in range(3):
            metadata = SummaryMetadata(
                citation_key=f"test2024paper{i}",
                input_words=1000 + i,
                input_chars=5000,
                output_words=200,
                compression_ratio=0.2,
                generation_time=30.0,
                words_per_second=6.67,
                quality_score=0.9,
                validation_errors=[],
                attempts=1,
                generated="2024-01-01T00:00:00"
            )
            manager.add_metadata(metadata)
        
        all_metadata = manager.get_all_metadata()
        
        assert len(all_metadata) == 3
        assert "test2024paper0" in all_metadata
        assert "test2024paper1" in all_metadata
        assert "test2024paper2" in all_metadata
    
    def test_remove_metadata(self, tmp_path):
        """Test removing metadata."""
        metadata_path = tmp_path / "metadata.json"
        manager = SummaryMetadataManager(metadata_path)
        
        # Add metadata
        metadata = SummaryMetadata(
            citation_key="test2024paper",
            input_words=1000,
            input_chars=5000,
            output_words=200,
            compression_ratio=0.2,
            generation_time=30.0,
            words_per_second=6.67,
            quality_score=0.9,
            validation_errors=[],
            attempts=1,
            generated="2024-01-01T00:00:00"
        )
        manager.add_metadata(metadata)
        
        # Verify it exists
        assert manager.get_metadata("test2024paper") is not None
        
        # Remove it
        manager.remove_metadata("test2024paper")
        
        # Verify it's gone
        assert manager.get_metadata("test2024paper") is None
        assert len(manager.get_all_metadata()) == 0
        
        # Verify file was updated
        with open(metadata_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            assert "test2024paper" not in data
    
    def test_remove_nonexistent_metadata(self, tmp_path):
        """Test removing non-existent metadata (should not error)."""
        metadata_path = tmp_path / "metadata.json"
        manager = SummaryMetadataManager(metadata_path)
        
        # Should not raise error
        manager.remove_metadata("nonexistent")
    
    def test_get_statistics_empty(self, tmp_path):
        """Test getting statistics with no metadata."""
        metadata_path = tmp_path / "metadata.json"
        manager = SummaryMetadataManager(metadata_path)
        
        stats = manager.get_statistics()
        
        assert stats["total_summaries"] == 0
        assert stats["avg_quality_score"] == 0.0
        assert stats["avg_compression_ratio"] == 0.0
        assert stats["total_input_words"] == 0
        assert stats["total_output_words"] == 0
    
    def test_get_statistics_with_data(self, tmp_path):
        """Test getting statistics with metadata."""
        metadata_path = tmp_path / "metadata.json"
        manager = SummaryMetadataManager(metadata_path)
        
        # Add multiple metadata entries
        metadata1 = SummaryMetadata(
            citation_key="test1",
            input_words=1000,
            input_chars=5000,
            output_words=200,
            compression_ratio=0.2,
            generation_time=30.0,
            words_per_second=6.67,
            quality_score=0.8,
            validation_errors=[],
            attempts=1,
            generated="2024-01-01T00:00:00"
        )
        
        metadata2 = SummaryMetadata(
            citation_key="test2",
            input_words=2000,
            input_chars=10000,
            output_words=400,
            compression_ratio=0.2,
            generation_time=60.0,
            words_per_second=6.67,
            quality_score=0.9,
            validation_errors=[],
            attempts=1,
            generated="2024-01-01T00:00:00"
        )
        
        manager.add_metadata(metadata1)
        manager.add_metadata(metadata2)
        
        stats = manager.get_statistics()
        
        assert stats["total_summaries"] == 2
        assert abs(stats["avg_quality_score"] - 0.85) < 0.01  # (0.8 + 0.9) / 2
        assert abs(stats["avg_compression_ratio"] - 0.2) < 0.01
        assert abs(stats["avg_generation_time"] - 45.0) < 0.01  # (30 + 60) / 2
        assert stats["total_input_words"] == 3000  # 1000 + 2000
        assert stats["total_output_words"] == 600  # 200 + 400
    
    def test_get_statistics_filters_zero_values(self, tmp_path):
        """Test that statistics filter out zero values."""
        metadata_path = tmp_path / "metadata.json"
        manager = SummaryMetadataManager(metadata_path)
        
        # Add metadata with zero quality score
        metadata = SummaryMetadata(
            citation_key="test1",
            input_words=1000,
            input_chars=5000,
            output_words=200,
            compression_ratio=0.2,
            generation_time=30.0,
            words_per_second=6.67,
            quality_score=0.0,  # Zero value
            validation_errors=[],
            attempts=1,
            generated="2024-01-01T00:00:00"
        )
        
        manager.add_metadata(metadata)
        
        stats = manager.get_statistics()
        
        # Should not include zero quality score in average
        assert stats["avg_quality_score"] == 0.0
        assert stats["total_summaries"] == 1
    
    def test_persistence_across_instances(self, tmp_path):
        """Test that metadata persists across manager instances."""
        metadata_path = tmp_path / "metadata.json"
        
        # Create first manager and add metadata
        manager1 = SummaryMetadataManager(metadata_path)
        metadata = SummaryMetadata(
            citation_key="test2024paper",
            input_words=1000,
            input_chars=5000,
            output_words=200,
            compression_ratio=0.2,
            generation_time=30.0,
            words_per_second=6.67,
            quality_score=0.9,
            validation_errors=[],
            attempts=1,
            generated="2024-01-01T00:00:00"
        )
        manager1.add_metadata(metadata)
        
        # Create second manager and verify it loads the metadata
        manager2 = SummaryMetadataManager(metadata_path)
        retrieved = manager2.get_metadata("test2024paper")
        
        assert retrieved is not None
        assert retrieved.citation_key == "test2024paper"
        assert retrieved.input_words == 1000

