#!/usr/bin/env python3
"""
Extract GitHub repository URLs and code language information from extracted text files.
"""

import re
import os
from pathlib import Path
from collections import defaultdict

# Pattern to find GitHub URLs
github_pattern = re.compile(r'https?://(?:www\.)?github\.com/[^\s\)]+|github\.com/[^\s\)]+', re.IGNORECASE)

# Pattern to find programming languages/technologies
code_patterns = {
    'Python': re.compile(r'\bpython\b', re.IGNORECASE),
    'MATLAB': re.compile(r'\bmatlab\b', re.IGNORECASE),
    'Julia': re.compile(r'\bjulia\b', re.IGNORECASE),
    'R': re.compile(r'\b\bR\b\b', re.IGNORECASE),
    'C++': re.compile(r'\bc\+\+\b', re.IGNORECASE),
    'Java': re.compile(r'\bjava\b', re.IGNORECASE),
    'JavaScript': re.compile(r'\bjavascript\b', re.IGNORECASE),
    'TypeScript': re.compile(r'\btypescript\b', re.IGNORECASE),
    'PyTorch': re.compile(r'\bpytorch\b', re.IGNORECASE),
    'TensorFlow': re.compile(r'\btensorflow\b', re.IGNORECASE),
    'JAX': re.compile(r'\bjax\b', re.IGNORECASE),
    'ROS': re.compile(r'\bros\b', re.IGNORECASE),
    'ROS2': re.compile(r'\bros2\b', re.IGNORECASE),
}

def clean_url(url):
    """Clean and normalize GitHub URL."""
    # Remove trailing punctuation and common suffixes
    url = url.rstrip('.,;:!?)')
    # Remove trailing year references like ",2019" or ",2020"
    url = re.sub(r',\s*\d{4}$', '', url)
    # Remove trailing version numbers like ",3" or ",2.0"
    url = re.sub(r',\s*\d+(?:\.\d+)?$', '', url)
    # Remove trailing paths that are incomplete (ending with /)
    if url.endswith('/') and url.count('/') > 4:
        url = url.rstrip('/')
    # Add https:// if missing
    if not url.startswith('http'):
        url = 'https://' + url
    return url

def find_code_mentions(content, github_urls, lines):
    """Find programming language mentions near GitHub URLs."""
    code_mentions = set()
    
    for i, line in enumerate(lines):
        if any(url.replace('https://', '').replace('http://', '') in line.lower() 
               for url in github_urls):
            # Check surrounding lines for code mentions
            context_start = max(0, i-10)
            context_end = min(len(lines), i+10)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            for lang, pattern in code_patterns.items():
                if pattern.search(context):
                    code_mentions.add(lang)
    
    # Also check the full content for general mentions
    content_lower = content.lower()
    for lang, pattern in code_patterns.items():
        if pattern.search(content_lower):
            code_mentions.add(lang)
    
    return code_mentions

def extract_github_info():
    """Extract GitHub URLs and code information from all extracted text files."""
    results = []
    extracted_text_dir = Path('data/extracted_text')
    
    if not extracted_text_dir.exists():
        print(f"Error: Directory {extracted_text_dir} does not exist")
        return []
    
    for txt_file in sorted(extracted_text_dir.glob('*.txt')):
        try:
            with open(txt_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
            
            # Find GitHub URLs
            github_urls_raw = github_pattern.findall(content)
            
            if github_urls_raw:
                # Clean up URLs
                cleaned_urls = []
                for url in github_urls_raw:
                    cleaned = clean_url(url)
                    if cleaned not in cleaned_urls:
                        cleaned_urls.append(cleaned)
                
                # Find code mentions
                code_mentions = find_code_mentions(content, cleaned_urls, lines)
                
                paper_name = txt_file.stem
                results.append({
                    'paper': paper_name,
                    'urls': cleaned_urls,
                    'languages': sorted(code_mentions) if code_mentions else ['Not specified']
                })
        except Exception as e:
            print(f'Error processing {txt_file}: {e}', file=os.sys.stderr)
    
    return results

def generate_markdown_report(results):
    """Generate a markdown report of all GitHub repositories."""
    output = []
    output.append("# GitHub Repositories Found in Literature\n")
    output.append(f"This document contains all GitHub repository URLs found in the extracted text files.\n")
    output.append(f"**Total papers with GitHub repositories: {len(results)}**\n")
    output.append("---\n\n")
    
    # Group by language if possible
    by_language = defaultdict(list)
    for result in results:
        lang_key = ', '.join(result['languages']) if result['languages'] != ['Not specified'] else 'Not specified'
        by_language[lang_key].append(result)
    
    # Sort languages
    sorted_langs = sorted(by_language.keys(), key=lambda x: (x == 'Not specified', x))
    
    for lang in sorted_langs:
        if lang != 'Not specified':
            output.append(f"## {lang}\n\n")
        else:
            output.append("## Not Specified\n\n")
        
        papers = sorted(by_language[lang], key=lambda x: x['paper'])
        for result in papers:
            output.append(f"### {result['paper']}\n\n")
            for url in result['urls']:
                output.append(f"- {url}\n")
            if result['languages'] != ['Not specified']:
                output.append(f"\n**Languages/Tools:** {', '.join(result['languages'])}\n")
            output.append("\n")
    
    # Also create a flat list
    output.append("\n---\n\n")
    output.append("## Complete List (Alphabetical by Paper)\n\n")
    
    for result in sorted(results, key=lambda x: x['paper']):
        output.append(f"### {result['paper']}\n\n")
        for url in result['urls']:
            output.append(f"- {url}\n")
        output.append(f"**Languages/Tools:** {', '.join(result['languages'])}\n\n")
    
    return ''.join(output)

if __name__ == '__main__':
    print("Extracting GitHub repository information...")
    results = extract_github_info()
    
    print(f"\nFound {len(results)} papers with GitHub repositories")
    
    # Generate markdown report
    report = generate_markdown_report(results)
    
    output_file = Path('data/github_repositories.md')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\nReport saved to: {output_file}")
    print(f"\nSummary:")
    for result in sorted(results, key=lambda x: x['paper'])[:10]:  # Show first 10
        print(f"  {result['paper']}: {len(result['urls'])} repo(s) - {', '.join(result['languages'])}")
    if len(results) > 10:
        print(f"  ... and {len(results) - 10} more")
