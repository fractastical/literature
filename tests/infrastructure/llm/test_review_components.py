#!/usr/bin/env python3
"""Comprehensive tests for LLM review components.

Tests review module components (generator, io, metrics) with real functionality.
No mocks - tests actual component behavior.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

# Add repo root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from infrastructure.llm.review.metrics import (
    ReviewMetrics,
    ManuscriptMetrics,
    SessionMetrics,
    StreamingMetrics,
    estimate_tokens,
)


class TestReviewMetrics:
    """Test ReviewMetrics dataclass."""
    
    def test_metrics_creation(self):
        """Test creating review metrics."""
        metrics = ReviewMetrics(
            input_chars=1000,
            input_words=150,
            input_tokens_est=250,
            output_chars=500,
            output_words=75,
            output_tokens_est=125,
            generation_time_seconds=2.5,
            preview="This is a preview..."
        )
        
        assert metrics.input_chars == 1000
        assert metrics.input_words == 150
        assert metrics.output_chars == 500
        assert metrics.generation_time_seconds == 2.5
    
    def test_metrics_defaults(self):
        """Test metrics with defaults."""
        metrics = ReviewMetrics(
            input_chars=100,
            input_words=15,
            input_tokens_est=25,
            output_chars=50,
            output_words=8,
            output_tokens_est=12,
            generation_time_seconds=1.0
        )
        
        assert metrics.preview == ""


class TestManuscriptMetrics:
    """Test ManuscriptMetrics dataclass."""
    
    def test_manuscript_metrics_creation(self):
        """Test creating manuscript metrics."""
        metrics = ManuscriptMetrics(
            total_chars=5000,
            total_words=750,
            total_tokens_est=1250,
            estimated_review_time_seconds=10.0
        )
        
        assert metrics.total_chars == 5000
        assert metrics.total_words == 750
        assert metrics.estimated_review_time_seconds == 10.0


class TestSessionMetrics:
    """Test SessionMetrics dataclass."""
    
    def test_session_metrics_creation(self):
        """Test creating session metrics."""
        metrics = SessionMetrics(
            total_reviews=5,
            total_generation_time=25.0,
            model_name="test_model"
        )
        
        assert metrics.total_reviews == 5
        assert metrics.total_generation_time == 25.0
        assert metrics.model_name == "test_model"


class TestStreamingMetrics:
    """Test StreamingMetrics."""
    
    def test_streaming_metrics_creation(self):
        """Test creating streaming metrics."""
        metrics = StreamingMetrics()
        
        assert metrics.total_chars == 0
        assert metrics.total_tokens_est == 0
    
    def test_streaming_metrics_update(self):
        """Test updating streaming metrics."""
        metrics = StreamingMetrics()
        metrics.update("New text chunk", 10)
        
        assert metrics.total_chars > 0
        assert metrics.total_tokens_est > 0


class TestEstimateTokens:
    """Test token estimation."""
    
    def test_estimate_tokens_simple(self):
        """Test token estimation for simple text."""
        text = "This is a test."
        tokens = estimate_tokens(text)
        
        assert isinstance(tokens, int)
        assert tokens > 0
    
    def test_estimate_tokens_empty(self):
        """Test token estimation for empty text."""
        tokens = estimate_tokens("")
        assert tokens == 0
    
    def test_estimate_tokens_long_text(self):
        """Test token estimation for long text."""
        text = "This is a test. " * 100
        tokens = estimate_tokens(text)
        
        assert isinstance(tokens, int)
        assert tokens > 0


class TestReviewGenerator:
    """Test review generator functions."""
    
    def test_get_manuscript_review_system_prompt(self):
        """Test getting system prompt."""
        from infrastructure.llm.review.generator import get_manuscript_review_system_prompt
        
        prompt = get_manuscript_review_system_prompt()
        assert isinstance(prompt, str)
        assert len(prompt) > 0
    
    def test_get_max_input_length(self):
        """Test getting max input length."""
        from infrastructure.llm.review.generator import get_max_input_length
        
        length = get_max_input_length()
        assert isinstance(length, int)
        assert length > 0
    
    def test_get_review_timeout(self):
        """Test getting review timeout."""
        from infrastructure.llm.review.generator import get_review_timeout
        
        timeout = get_review_timeout()
        assert isinstance(timeout, (int, float))
        assert timeout > 0
    
    def test_get_review_max_tokens(self):
        """Test getting review max tokens."""
        from infrastructure.llm.review.generator import get_review_max_tokens
        
        max_tokens = get_review_max_tokens()
        assert isinstance(max_tokens, int)
        assert max_tokens > 0
    
    def test_extract_manuscript_text(self, tmp_path):
        """Test extracting manuscript text from file."""
        from infrastructure.llm.review.generator import extract_manuscript_text
        
        # Create test file
        test_file = tmp_path / "test.txt"
        test_file.write_text("This is test manuscript text.")
        
        text = extract_manuscript_text(test_file)
        assert isinstance(text, str)
        assert "test manuscript" in text


class TestReviewIO:
    """Test review I/O functions."""
    
    def test_extract_action_items(self):
        """Test extracting action items from review."""
        from infrastructure.llm.review.io import extract_action_items
        
        review_text = """
        This is a review.
        
        Action items:
        1. Fix the methodology section
        2. Add more references
        3. Improve the conclusion
        """
        
        items = extract_action_items(review_text)
        assert isinstance(items, str)
        assert len(items) > 0
    
    def test_calculate_format_compliance_summary(self):
        """Test calculating format compliance."""
        from infrastructure.llm.review.io import calculate_format_compliance_summary
        
        reviews = {
            "executive_summary": "Review text here",
            "quality_review": "Another review"
        }
        
        summary = calculate_format_compliance_summary(reviews)
        assert isinstance(summary, str)
    
    def test_calculate_quality_summary(self):
        """Test calculating quality summary."""
        from infrastructure.llm.review.io import calculate_quality_summary
        
        reviews = {
            "executive_summary": "Review with quality score: 4/5",
            "quality_review": "Another review"
        }
        
        summary = calculate_quality_summary(reviews)
        assert isinstance(summary, str)
    
    def test_save_single_review(self, tmp_path):
        """Test saving a single review."""
        from infrastructure.llm.review.io import save_single_review
        from infrastructure.llm.review.metrics import ReviewMetrics
        
        output_dir = tmp_path / "reviews"
        output_dir.mkdir()
        
        metrics = ReviewMetrics(
            input_chars=100,
            input_words=15,
            input_tokens_est=25,
            output_chars=50,
            output_words=8,
            output_tokens_est=12,
            generation_time_seconds=1.0
        )
        
        path = save_single_review(
            "test_review",
            "Review content here",
            output_dir,
            "test_model",
            metrics
        )
        
        assert isinstance(path, Path)
        assert path.exists()


class TestReviewModuleImports:
    """Test that review module imports correctly."""
    
    def test_review_module_imports(self):
        """Test review module imports."""
        from infrastructure.llm import review
        assert review is not None
    
    def test_generator_imports(self):
        """Test generator module imports."""
        from infrastructure.llm.review import generator
        assert generator is not None
    
    def test_io_imports(self):
        """Test io module imports."""
        from infrastructure.llm.review import io
        assert io is not None
    
    def test_metrics_imports(self):
        """Test metrics module imports."""
        from infrastructure.llm.review import metrics
        assert metrics is not None

