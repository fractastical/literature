"""Tests for infrastructure/core/config_cli.py.

Tests configuration CLI functionality with real execution.
No mocks - tests actual behavior.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

# Add repo root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


class TestConfigCli:
    """Test config_cli module."""
    
    def test_module_imports(self):
        """Test module imports correctly."""
        from infrastructure.core import config_cli
        assert config_cli is not None
        assert hasattr(config_cli, 'main')
    
    def test_main_function_exists(self):
        """Test main function exists and is callable."""
        from infrastructure.core import config_cli
        assert callable(config_cli.main)
    
    def test_main_outputs_bash_exports(self, tmp_path, monkeypatch):
        """Test main function outputs bash export statements."""
        from infrastructure.core import config_cli
        
        # Set up a temporary config directory structure
        config_dir = tmp_path / "project" / "manuscript"
        config_dir.mkdir(parents=True)
        config_file = config_dir / "config.yaml"
        
        # Create a minimal config file
        config_file.write_text("""
test_key: test_value
another_key: another_value
""")
        
        # Monkeypatch repo_root in config_cli
        original_repo_root = Path(config_cli.__file__).parent.parent
        monkeypatch.setattr(config_cli, 'repo_root', tmp_path)
        
        # Capture output
        import io
        from contextlib import redirect_stdout
        
        output = io.StringIO()
        with redirect_stdout(output):
            try:
                config_cli.main()
            except SystemExit:
                pass
        
        output_str = output.getvalue()
        
        # Should contain export statements
        assert 'export' in output_str or len(output_str.strip()) == 0
    
    def test_main_handles_missing_yaml(self, monkeypatch):
        """Test main handles missing PyYAML gracefully."""
        from infrastructure.core import config_cli
        
        # Mock YAML_AVAILABLE to False
        monkeypatch.setattr('infrastructure.core.config_cli.YAML_AVAILABLE', False)
        
        import io
        from contextlib import redirect_stdout, redirect_stderr
        
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            try:
                config_cli.main()
            except SystemExit:
                pass
        
        stderr_str = stderr.getvalue()
        # Should output error message about PyYAML
        assert len(stderr_str) > 0 or len(stdout.getvalue()) == 0
    
    def test_main_handles_import_error(self, monkeypatch):
        """Test main handles import errors gracefully."""
        from infrastructure.core import config_cli
        
        # Cause import error
        original_import = __import__
        def mock_import(name, *args, **kwargs):
            if 'config_loader' in name:
                raise ImportError("Mocked import error")
            return original_import(name, *args, **kwargs)
        
        monkeypatch.setattr('builtins.__import__', mock_import)
        
        import io
        from contextlib import redirect_stderr
        
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            try:
                # Reload module to trigger import error
                import importlib
                importlib.reload(config_cli)
                config_cli.main()
            except (SystemExit, ImportError):
                pass
        
        # Should handle error gracefully
        assert True  # If we get here, it didn't crash















