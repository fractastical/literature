#!/usr/bin/env python3
"""Tests for summary parser.

Tests SummaryMetadata dataclass and SummaryParser with real markdown parsing.
No mocks - tests actual component behavior.
"""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from infrastructure.literature.summarization.parser import (
    SummaryMetadata,
    SummaryParser,
)


class TestSummaryMetadata:
    """Test SummaryMetadata dataclass."""
    
    def test_metadata_creation(self):
        """Test creating summary metadata."""
        metadata = SummaryMetadata(
            citation_key="test2024paper",
            title="Test Paper Title",
            authors=["Author One", "Author Two"],
            year=2024,
            source="arxiv",
            venue="arXiv preprint",
            doi="10.1234/example.doi",
            pdf_path="data/pdfs/test2024paper.pdf",
            generated_date="2024-01-01T00:00:00"
        )
        
        assert metadata.citation_key == "test2024paper"
        assert metadata.title == "Test Paper Title"
        assert len(metadata.authors) == 2
        assert metadata.year == 2024
        assert metadata.source == "arxiv"
        assert metadata.keywords == []  # Default empty list
        assert metadata.concepts == []  # Default empty list
    
    def test_metadata_defaults(self):
        """Test metadata with default values."""
        metadata = SummaryMetadata(
            citation_key="test2024paper",
            title="Test Paper",
            authors=[],
            year=None,
            source="unknown",
            venue=None,
            doi=None,
            pdf_path=None,
            generated_date=None
        )
        
        assert metadata.overview is None
        assert metadata.key_contributions is None
        assert metadata.methodology is None
        assert metadata.results is None
        assert metadata.limitations is None
        assert metadata.discussion is None
        assert metadata.keywords == []
        assert metadata.concepts == []
    
    def test_metadata_to_dict(self):
        """Test converting metadata to dictionary."""
        metadata = SummaryMetadata(
            citation_key="test2024paper",
            title="Test Paper",
            authors=["Author One"],
            year=2024,
            source="arxiv",
            venue=None,
            doi=None,
            pdf_path=None,
            generated_date=None
        )
        
        data = metadata.to_dict()
        
        assert isinstance(data, dict)
        assert data["citation_key"] == "test2024paper"
        assert data["title"] == "Test Paper"
        assert data["authors"] == ["Author One"]


class TestSummaryParser:
    """Test SummaryParser class."""
    
    def test_parse_summary_content_basic(self):
        """Test parsing basic summary content."""
        parser = SummaryParser()
        
        content = """
# Test Paper Title

**Authors:** Author One, Author Two
**Year:** 2024
**Source:** arxiv
**Venue:** arXiv preprint
**DOI:** 10.1234/example.doi
**Generated:** 2024-01-01T00:00:00

---

## Overview

This is the overview section.

## Key Contributions

This paper contributes X, Y, and Z.

## Methodology

The methodology involves A and B.

## Results

The results show significant improvements.

## Limitations

Some limitations exist.

## Discussion

The discussion covers implications.
"""
        
        metadata = parser.parse_summary_content(content, citation_key="test2024paper")
        
        assert metadata.citation_key == "test2024paper"
        assert metadata.title == "Test Paper Title"
        assert len(metadata.authors) == 2
        assert metadata.authors[0] == "Author One"
        assert metadata.year == 2024
        assert metadata.source == "arxiv"
        assert metadata.venue == "arXiv preprint"
        assert metadata.doi == "10.1234/example.doi"
        assert "overview" in metadata.overview.lower()
        assert metadata.key_contributions is not None
        assert "paper" in metadata.key_contributions.lower()
        assert "methodology" in metadata.methodology.lower()
        assert "results" in metadata.results.lower()
    
    def test_parse_summary_content_minimal(self):
        """Test parsing minimal summary content."""
        parser = SummaryParser()
        
        content = """
# Test Paper

**Authors:** Author One
**Year:** 2024
**Source:** arxiv

---

## Overview

This is a minimal summary.
"""
        
        metadata = parser.parse_summary_content(content, citation_key="test2024paper")
        
        assert metadata.citation_key == "test2024paper"
        assert metadata.title == "Test Paper"
        assert len(metadata.authors) == 1
        assert metadata.year == 2024
        assert metadata.overview is not None
        assert metadata.key_contributions is None
        assert metadata.methodology is None
    
    def test_parse_summary_content_with_statistics(self):
        """Test parsing summary with statistics."""
        parser = SummaryParser()
        
        content = """
# Test Paper

**Authors:** Author One
**Year:** 2024
**Source:** arxiv

---

## Overview

This is the overview.

Summary Statistics:
Input: 1,000 words (5,000 chars)
Output: 200 words
Compression: 0.2x
Generation: 30.5s
Quality Score: 0.9/
Attempts: 1
"""
        
        metadata = parser.parse_summary_content(content, citation_key="test2024paper")
        
        assert metadata.input_words == 1000
        assert metadata.input_chars == 5000
        assert metadata.output_words == 200
        assert abs(metadata.compression_ratio - 0.2) < 0.01
        assert abs(metadata.generation_time - 30.5) < 0.01
        assert abs(metadata.quality_score - 0.9) < 0.01
        assert metadata.attempts == 1
    
    def test_parse_summary_content_keywords(self):
        """Test keyword extraction."""
        parser = SummaryParser()
        
        content = """
# Test Paper

**Authors:** Author One
**Year:** 2024
**Source:** arxiv

---

## Overview

This paper discusses machine learning algorithms and neural networks. 
The methodology involves deep learning techniques and optimization methods.
Results show significant improvements in performance metrics.
"""
        
        metadata = parser.parse_summary_content(content, citation_key="test2024paper")
        
        assert len(metadata.keywords) > 0
        # Should extract relevant keywords
        keywords_lower = [k.lower() for k in metadata.keywords]
        assert any("learning" in k or "machine" in k for k in keywords_lower)
    
    def test_parse_summary_content_concepts(self):
        """Test concept extraction."""
        parser = SummaryParser()
        
        content = """
# Test Paper

**Authors:** Author One
**Year:** 2024
**Source:** arxiv

---

## Overview

This paper discusses "Machine Learning" and "Neural Networks". 
The methodology involves Deep Learning Techniques and Optimization Methods.
"""
        
        metadata = parser.parse_summary_content(content, citation_key="test2024paper")
        
        assert len(metadata.concepts) > 0
        concepts_str = " ".join(metadata.concepts)
        assert "Machine Learning" in concepts_str or "Neural Networks" in concepts_str
    
    def test_parse_summary_file(self, tmp_path):
        """Test parsing summary file."""
        parser = SummaryParser()
        
        summary_file = tmp_path / "test2024paper_summary.md"
        content = """
# Test Paper

**Authors:** Author One
**Year:** 2024
**Source:** arxiv

---

## Overview

This is the overview.
"""
        
        summary_file.write_text(content, encoding="utf-8")
        
        metadata = parser.parse_summary_file(summary_file)
        
        assert metadata.citation_key == "test2024paper"
        assert metadata.title == "Test Paper"
    
    def test_extract_header_metadata_unknown_year(self):
        """Test parsing with unknown year."""
        parser = SummaryParser()
        
        content = """
# Test Paper

**Authors:** Author One
**Year:** Unknown
**Source:** arxiv

---

## Overview

Content here.
"""
        
        metadata = parser.parse_summary_content(content, citation_key="test2024paper")
        
        assert metadata.year is None
    
    def test_extract_header_metadata_na_venue(self):
        """Test parsing with N/A venue."""
        parser = SummaryParser()
        
        content = """
# Test Paper

**Authors:** Author One
**Year:** 2024
**Source:** arxiv
**Venue:** N/A

---

## Overview

Content here.
"""
        
        metadata = parser.parse_summary_content(content, citation_key="test2024paper")
        
        assert metadata.venue is None
    
    def test_extract_header_metadata_pdf_link(self):
        """Test extracting PDF path from link."""
        parser = SummaryParser()
        
        content = """
# Test Paper

**Authors:** Author One
**Year:** 2024
**Source:** arxiv
**PDF:** [Download PDF](data/pdfs/test2024paper.pdf)

---

## Overview

Content here.
"""
        
        metadata = parser.parse_summary_content(content, citation_key="test2024paper")
        
        assert metadata.pdf_path == "data/pdfs/test2024paper.pdf"
    
    def test_extract_sections_various_formats(self):
        """Test extracting sections with various header formats."""
        parser = SummaryParser()
        
        content = """
# Test Paper

**Authors:** Author One
**Year:** 2024
**Source:** arxiv

---

### Overview

This is overview with ### header.

## Key Contributions

This is contributions with ## header.

### Methods

This is methods section.

## Results

This is results section.
"""
        
        metadata = parser.parse_summary_content(content, citation_key="test2024paper")
        
        assert metadata.overview is not None
        assert "overview" in metadata.overview.lower()
        assert metadata.key_contributions is not None
        assert metadata.methodology is not None
        assert metadata.results is not None
    
    def test_export_metadata(self, tmp_path):
        """Test exporting metadata to JSON."""
        parser = SummaryParser()
        
        metadata = SummaryMetadata(
            citation_key="test2024paper",
            title="Test Paper",
            authors=["Author One"],
            year=2024,
            source="arxiv",
            venue=None,
            doi=None,
            pdf_path=None,
            generated_date=None
        )
        
        output_path = tmp_path / "metadata.json"
        parser.export_metadata(metadata, output_path)
        
        assert output_path.exists()
        with open(output_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            assert data["citation_key"] == "test2024paper"
            assert data["title"] == "Test Paper"
    
    def test_batch_parse_summaries(self, tmp_path):
        """Test batch parsing multiple summaries."""
        parser = SummaryParser()
        
        # Create multiple summary files
        summaries_dir = tmp_path / "summaries"
        summaries_dir.mkdir()
        
        for i in range(3):
            summary_file = summaries_dir / f"test{i}_summary.md"
            content = f"""
# Test Paper {i}

**Authors:** Author {i}
**Year:** 2024
**Source:** arxiv

---

## Overview

This is paper {i}.
"""
            summary_file.write_text(content, encoding="utf-8")
        
        summaries = parser.batch_parse_summaries(summaries_dir)
        
        assert len(summaries) == 3
        # Files may be processed in any order, so check all keys are present
        citation_keys = {s.citation_key for s in summaries}
        assert citation_keys == {"test0", "test1", "test2"}
    
    def test_batch_parse_summaries_invalid_file(self, tmp_path):
        """Test batch parsing with invalid file (should skip gracefully)."""
        parser = SummaryParser()
        
        summaries_dir = tmp_path / "summaries"
        summaries_dir.mkdir()
        
        # Create valid file
        valid_file = summaries_dir / "test0_summary.md"
        valid_file.write_text("# Test\n**Authors:** Author\n**Year:** 2024\n**Source:** arxiv\n---\n## Overview\nContent", encoding="utf-8")
        
        # Create invalid file (not a summary file)
        invalid_file = summaries_dir / "other_file.md"
        invalid_file.write_text("Not a summary", encoding="utf-8")
        
        summaries = parser.batch_parse_summaries(summaries_dir)
        
        # Should only parse summary files
        assert len(summaries) == 1
        assert summaries[0].citation_key == "test0"
    
    def test_export_batch_metadata(self, tmp_path):
        """Test exporting batch metadata to JSON."""
        parser = SummaryParser()
        
        summaries_dir = tmp_path / "summaries"
        summaries_dir.mkdir()
        
        # Create summary files
        for i in range(2):
            summary_file = summaries_dir / f"test{i}_summary.md"
            content = f"""
# Test Paper {i}

**Authors:** Author {i}
**Year:** 2024
**Source:** arxiv

---

## Overview

This is paper {i}.
"""
            summary_file.write_text(content, encoding="utf-8")
        
        output_path = tmp_path / "batch_metadata.json"
        parser.export_batch_metadata(summaries_dir, output_path)
        
        assert output_path.exists()
        with open(output_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            assert data["total_summaries"] == 2
            assert len(data["summaries"]) == 2
            assert "metadata_version" in data
            assert "generated_at" in data
    
    def test_parse_empty_content(self):
        """Test parsing empty content."""
        parser = SummaryParser()
        
        content = ""
        
        metadata = parser.parse_summary_content(content, citation_key="test2024paper")
        
        assert metadata.citation_key == "test2024paper"
        assert metadata.title == ""
        assert metadata.authors == []
    
    def test_parse_content_no_sections(self):
        """Test parsing content without sections."""
        parser = SummaryParser()
        
        content = """
# Test Paper

**Authors:** Author One
**Year:** 2024
**Source:** arxiv

---

No sections here, just plain text.
"""
        
        metadata = parser.parse_summary_content(content, citation_key="test2024paper")
        
        assert metadata.citation_key == "test2024paper"
        assert metadata.overview is None
        assert metadata.key_contributions is None

