#!/usr/bin/env bash

################################################################################
# Literature Operations Orchestrator
#
# Entry point for literature search and management operations with interactive menu:
#
# Orchestrated Pipelines:
#   0. Full Pipeline (search → download → extract → summarize)
#   1. Meta-Analysis Pipeline (search → download → extract → meta-analysis)
#
# Individual Operations (via 07_literature_search.py):
#   2. Search Only (network only - add to bibliography)
#   3. Download Only (network only - download PDFs)
#   4. Extract Text (local only - extract text from PDFs)
#   5. Summarize (requires Ollama - generate summaries)
#   6. Cleanup (local files only - remove papers without PDFs)
#   7. Advanced LLM Operations (requires Ollama)
#   9. Run Test Suite (with coverage analysis)
#   8. Exit
#
# Non-interactive mode: Use dedicated flags (--search, --download, etc.)
#
# Exit codes: 0 = success, 1 = failure, 2 = skipped (for optional stages)
################################################################################

set -euo pipefail

# Source shared utilities
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$SCRIPT_DIR"
source "$SCRIPT_DIR/scripts/bash_utils.sh"

# ============================================================================
# Menu Display
# ============================================================================

get_library_stats_display() {
    # Get library statistics using Python helper
    cd "$REPO_ROOT" || return
    python3 << 'PYTHON_EOF'
import sys
from pathlib import Path

try:
    from infrastructure.literature.library.stats import get_library_statistics, format_library_stats_display
    stats = get_library_statistics()
    print(format_library_stats_display(stats))
except Exception as e:
    print("  • Library: Not available")
PYTHON_EOF
}

display_menu() {
    clear
    echo -e "${BOLD}${BLUE}"
    echo "============================================================"
    echo "  Literature Operations Menu"
    echo "============================================================"
    echo -e "${NC}"
    echo
    
    # Display library statistics
    echo -e "${BOLD}${CYAN}Current Library Status:${NC}"
    get_library_stats_display
    echo
    
    echo -e "${BOLD}Orchestrated Pipelines:${NC}"
    echo -e "  0. ${GREEN}Full Pipeline${NC} ${YELLOW}(search → download → extract → summarize)${NC}"
    echo -e "  1. ${GREEN}Meta-Analysis Pipeline${NC} ${YELLOW}(search → download → extract → meta-analysis)${NC}"
    echo
    echo -e "${BOLD}Individual Operations (via 07_literature_search.py):${NC}"
    echo -e "  2. Search Only ${CYAN}(network only - add to bibliography)${NC}"
    echo -e "  3. Download Only ${CYAN}(network only - download PDFs)${NC}"
    echo -e "  4. Extract Text ${CYAN}(local only - extract text from PDFs)${NC}"
    echo -e "  5. Summarize ${YELLOW}(requires Ollama - generate summaries)${NC}"
    echo -e "  6. Cleanup ${CYAN}(local files only - remove papers without PDFs)${NC}"
    echo -e "  7. Advanced LLM Operations ${YELLOW}(requires Ollama)${NC}"
    echo
    echo -e "${BOLD}Testing:${NC}"
    echo -e "  9. Run Test Suite ${CYAN}(with coverage analysis)${NC}"
    echo
    echo "  8. Exit"
    echo
    echo -e "${BLUE}============================================================${NC}"
    echo -e "  Repository: ${CYAN}$REPO_ROOT${NC}"
    echo -e "  Python: ${CYAN}$(python3 --version 2>&1)${NC}"
    echo -e "${BLUE}============================================================${NC}"
    echo
}

# ============================================================================
# Literature Operation Functions
# ============================================================================

run_literature_search_all() {
    # Run orchestrated literature pipeline: search → download → extract → summarize
    log_header "ORCHESTRATED LITERATURE PIPELINE"
    
    cd "$REPO_ROOT"
    
    echo
    log_info "🔄 Starting orchestrated literature pipeline..."
    echo
    log_info "Pipeline stages:"
    log_info "  1️⃣  Search academic databases for keywords"
    log_info "  2️⃣  Download PDFs from available sources"
    log_info "  3️⃣  Extract text from PDFs (save to extracted_text/)"
    log_info "  4️⃣  Generate AI-powered summaries (requires Ollama)"
    echo
    log_info "You will be prompted for:"
    log_info "  • Search keywords (comma-separated)"
    log_info "  • Number of results per keyword (default: 25)"
    log_info "  • Clear options (PDFs/Summaries/Library - default: No)"
    echo
    
    local start_time=$(date +%s)
    
    # Use --search which runs the full pipeline interactively
    # Clear options are handled interactively in the Python script
    if python3 scripts/07_literature_search.py --search; then
        local end_time=$(date +%s)
        local duration=$(get_elapsed_time "$start_time" "$end_time")
        echo
        log_success "✅ Orchestrated literature pipeline complete in $(format_duration "$duration")"
        echo
        log_info "📁 Output locations:"
        log_info "  • Bibliography: data/references.bib"
        log_info "  • JSON index: data/library.json"
        log_info "  • PDFs: data/pdfs/"
        log_info "  • Summaries: data/summaries/"
        echo
        return 0
    else
        log_error "❌ Orchestrated literature pipeline failed"
        return 1
    fi
}

run_literature_meta_analysis() {
    # Run orchestrated meta-analysis pipeline: search → download → extract → meta-analysis
    log_header "ORCHESTRATED META-ANALYSIS PIPELINE"
    
    cd "$REPO_ROOT"
    
    echo
    log_info "🔄 Starting meta-analysis pipeline..."
    echo
    log_info "Pipeline stages:"
    log_info "  1️⃣  Search academic databases for keywords"
    log_info "  2️⃣  Download PDFs from available sources"
    log_info "  3️⃣  Extract text from PDFs (save to extracted_text/)"
    log_info "  4️⃣  Perform meta-analysis (PCA, keywords, authors, visualizations)"
    echo
    log_info "You will be prompted for:"
    log_info "  • Search keywords (comma-separated)"
    log_info "  • Number of results per keyword (default: 25)"
    log_info "  • Clear options (PDFs/Library - default: No)"
    echo
    
    local start_time=$(date +%s)
    
    # Use --meta-analysis which runs the meta-analysis pipeline interactively
    # Clear options are handled interactively in the Python script
    if python3 scripts/07_literature_search.py --meta-analysis; then
        local end_time=$(date +%s)
        local duration=$(get_elapsed_time "$start_time" "$end_time")
        echo
        log_success "✅ Meta-analysis pipeline complete in $(format_duration "$duration")"
        echo
        log_info "📁 Output locations:"
        log_info "  • Bibliography: data/references.bib"
        log_info "  • JSON index: data/library.json"
        log_info "  • PDFs: data/pdfs/"
        log_info "  • Extracted text: data/extracted_text/"
        log_info "  • Visualizations: data/output/"
        echo
        return 0
    else
        log_error "❌ Meta-analysis pipeline failed"
        return 1
    fi
}

run_literature_search() {
    # Network-only operation: Searches arXiv and Semantic Scholar APIs
    # Does NOT require Ollama
    log_header "LITERATURE SEARCH (ADD TO BIBLIOGRAPHY)"

    cd "$REPO_ROOT"

    log_info "Searching literature and adding papers to bibliography (network only)..."

    if python3 scripts/07_literature_search.py --search-only; then
        log_success "Literature search complete"
        return 0
    else
        log_error "Literature search failed"
        return 1
    fi
}

run_literature_download() {
    # Network-only operation: Downloads PDFs via HTTP
    # Does NOT require Ollama
    log_header "DOWNLOAD PDFs (FOR BIBLIOGRAPHY ENTRIES)"

    cd "$REPO_ROOT"

    log_info "Downloading PDFs for bibliography entries without PDFs (network only)..."

    if python3 scripts/07_literature_search.py --download-only; then
        log_success "PDF download complete"
        return 0
    else
        log_error "PDF download failed"
        return 1
    fi
}

run_literature_extract_text() {
    log_header "EXTRACT TEXT FROM PDFs"

    cd "$REPO_ROOT"

    log_info "Extracting text from PDFs (local operation, no network required)..."
    if python3 scripts/07_literature_search.py --extract-text; then
        log_success "Text extraction complete!"
        return 0
    else
        log_error "Text extraction failed"
        return 1
    fi
}

run_literature_summarize() {
    log_header "GENERATE SUMMARIES (FOR PAPERS WITH PDFs)"

    cd "$REPO_ROOT"

    log_info "Generating summaries for papers with PDFs (requires Ollama)..."

    if python3 scripts/07_literature_search.py --summarize; then
        log_success "Summary generation complete"
        return 0
    else
        log_error "Summary generation failed"
        return 1
    fi
}

run_literature_cleanup() {
    # Local files-only operation: Removes files from filesystem
    # Does NOT require Ollama or network
    log_header "CLEANUP LIBRARY (REMOVE PAPERS WITHOUT PDFs)"

    cd "$REPO_ROOT"

    log_info "Cleaning up library by removing papers without PDFs (local files only)..."

    if python3 scripts/07_literature_search.py --cleanup; then
        log_success "Library cleanup complete"
        return 0
    else
        log_error "Library cleanup failed"
        return 1
    fi
}

run_literature_llm_operations() {
    log_header "ADVANCED LLM OPERATIONS (LITERATURE REVIEW, ETC.)"

    cd "$REPO_ROOT"

    echo
    echo "Available LLM operations:"
    echo "  1. Literature review synthesis"
    echo "  2. Science communication narrative"
    echo "  3. Comparative analysis"
    echo "  4. Research gap identification"
    echo "  5. Citation network analysis"
    echo

    read -p "Choose operation (1-5): " op_choice

    case $op_choice in
        1)
            operation="review"
            ;;
        2)
            operation="communication"
            ;;
        3)
            operation="compare"
            ;;
        4)
            operation="gaps"
            ;;
        5)
            operation="network"
            ;;
        *)
            log_error "Invalid choice: $op_choice"
            return 1
            ;;
    esac

    log_info "Running LLM operation: $operation (requires Ollama)..."

    if python3 scripts/07_literature_search.py --llm-operation "$operation"; then
        log_success "LLM operation complete"
        return 0
    else
        log_error "LLM operation failed"
        return 1
    fi
}

check_ollama_running() {
    # Check if Ollama is running using Python helper
    cd "$REPO_ROOT" || return 1
    python3 << 'PYTHON_EOF'
import sys
try:
    from infrastructure.llm.utils.ollama import is_ollama_running
    if is_ollama_running():
        print("true")
        sys.exit(0)
    else:
        print("false")
        sys.exit(0)
except Exception:
    print("false")
    sys.exit(0)
PYTHON_EOF
}

run_test_suite() {
    log_header "RUN TEST SUITE (WITH COVERAGE ANALYSIS)"

    cd "$REPO_ROOT"

    echo
    log_info "Checking test environment..."

    # Check if pytest is installed
    if ! command -v pytest &> /dev/null; then
        log_error "pytest is not installed"
        log_info "Install with: pip install pytest pytest-cov"
        return 1
    fi

    # Check if pytest-cov is installed
    if ! python3 -c "import pytest_cov" 2>/dev/null; then
        log_error "pytest-cov is not installed"
        log_info "Install with: pip install pytest-cov"
        return 1
    fi

    # Check Ollama availability
    log_info "Checking Ollama availability..."
    local ollama_available
    ollama_available=$(check_ollama_running)
    
    local pytest_args=()
    local test_mode=""
    
    if [[ "$ollama_available" == "true" ]]; then
        log_success "Ollama is running - will include all tests (including requires_ollama)"
        test_mode="full"
    else
        log_warning "Ollama is not running - will skip requires_ollama tests"
        pytest_args+=("-m" "not requires_ollama")
        test_mode="partial"
    fi

    echo
    log_info "Running test suite with coverage analysis..."
    log_info "Test mode: $test_mode"
    echo

    local start_time=$(date +%s)
    local test_output_file
    test_output_file=$(mktemp)
    local coverage_output_file
    coverage_output_file=$(mktemp)

    # Run pytest with coverage
    # Capture both stdout and stderr
    # Note: Excluding test_llm_review.py due to import errors (tests script that doesn't exist in this repo)
    local pytest_cmd=(
        pytest
        --cov=infrastructure
        --cov-report=term
        --cov-report=term-missing
        --cov-report=html
        --tb=short
        -v
        --ignore=tests/infrastructure/llm/test_llm_review.py
    )
    
    # Add Ollama marker filter if needed
    if [[ ${#pytest_args[@]} -gt 0 ]]; then
        pytest_cmd+=("${pytest_args[@]}")
    fi
    
    pytest_cmd+=(tests/)
    
    if "${pytest_cmd[@]}" > "$test_output_file" 2>&1; then
        local test_exit_code=0
    else
        local test_exit_code=$?
    fi

    local end_time=$(date +%s)
    local duration=$(get_elapsed_time "$start_time" "$end_time")

    # Display test output
    cat "$test_output_file"

    echo
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BOLD}TEST SUITE SUMMARY${NC}"
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo

    # Parse test results
    local total_tests passed_tests failed_tests skipped_tests
    total_tests=$(grep -E "passed|failed|skipped" "$test_output_file" | tail -1 | grep -oE "[0-9]+ passed" | grep -oE "[0-9]+" || echo "0")
    passed_tests=$(grep -E "passed|failed|skipped" "$test_output_file" | tail -1 | grep -oE "[0-9]+ passed" | grep -oE "[0-9]+" || echo "0")
    failed_tests=$(grep -E "passed|failed|skipped" "$test_output_file" | tail -1 | grep -oE "[0-9]+ failed" | grep -oE "[0-9]+" || echo "0")
    skipped_tests=$(grep -E "passed|failed|skipped" "$test_output_file" | tail -1 | grep -oE "[0-9]+ skipped" | grep -oE "[0-9]+" || echo "0")

    if [[ -n "$total_tests" ]] && [[ "$total_tests" != "0" ]]; then
        log_info "Total tests: $total_tests"
        if [[ "$passed_tests" != "0" ]]; then
            log_success "Passed: $passed_tests"
        fi
        if [[ "$failed_tests" != "0" ]]; then
            log_error "Failed: $failed_tests"
        fi
        if [[ "$skipped_tests" != "0" ]]; then
            log_warning "Skipped: $skipped_tests"
        fi
    else
        # Try alternative parsing
        local summary_line
        summary_line=$(grep -E "===.*passed.*failed.*skipped|passed.*failed.*skipped.*in" "$test_output_file" | tail -1 || echo "")
        if [[ -n "$summary_line" ]]; then
            log_info "Test summary: $summary_line"
        fi
    fi

    echo
    log_info "Duration: $(format_duration "$duration")"

    # Parse coverage results
    echo
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BOLD}COVERAGE ANALYSIS${NC}"
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo

    # Extract coverage summary
    local coverage_summary
    coverage_summary=$(grep -A 20 "TOTAL" "$test_output_file" | head -25 || echo "")
    
    if [[ -n "$coverage_summary" ]]; then
        echo "$coverage_summary"
    else
        log_warning "Could not parse coverage summary from output"
    fi

    # Check for coverage threshold (60% from pyproject.toml)
    local total_coverage
    total_coverage=$(grep "TOTAL" "$test_output_file" | grep -oE "[0-9]+%" | head -1 | grep -oE "[0-9]+" || echo "")
    
    if [[ -n "$total_coverage" ]]; then
        echo
        if [[ "$total_coverage" -ge 60 ]]; then
            log_success "Overall coverage: ${total_coverage}% (meets 60% threshold)"
        else
            log_warning "Overall coverage: ${total_coverage}% (below 60% threshold)"
        fi
    fi

    # Check for HTML coverage report
    if [[ -d "htmlcov" ]]; then
        echo
        log_info "📊 HTML coverage report generated: htmlcov/index.html"
        log_info "   Open with: open htmlcov/index.html"
    fi

    # List failed tests if any
    if [[ "$failed_tests" != "0" ]] || [[ "$test_exit_code" != "0" ]]; then
        echo
        echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
        echo -e "${BOLD}FAILED TESTS${NC}"
        echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
        echo
        
        # Extract failed test names
        local failed_test_lines
        failed_test_lines=$(grep -E "FAILED|ERROR" "$test_output_file" | head -20 || echo "")
        if [[ -n "$failed_test_lines" ]]; then
            echo "$failed_test_lines"
        else
            log_info "Review test output above for failure details"
        fi
    fi

    # Cleanup temp files
    rm -f "$test_output_file" "$coverage_output_file"

    echo
    if [[ "$test_exit_code" == "0" ]]; then
        log_success "✅ Test suite completed successfully"
        return 0
    else
        log_error "❌ Test suite completed with failures (exit code: $test_exit_code)"
        return 1
    fi
}

# ============================================================================
# Menu Handler
# ============================================================================

handle_menu_choice() {
    local choice="$1"
    local start_time end_time duration
    local exit_code=0
    
    start_time=$(date +%s)
    
    case "$choice" in
        0)
            run_literature_search_all
            exit_code=$?
            ;;
        1)
            run_literature_meta_analysis
            exit_code=$?
            ;;
        2)
            run_literature_search
            exit_code=$?
            ;;
        3)
            run_literature_download
            exit_code=$?
            ;;
        4)
            run_literature_extract_text
            exit_code=$?
            ;;
        5)
            run_literature_summarize
            exit_code=$?
            ;;
        6)
            run_literature_cleanup
            exit_code=$?
            ;;
        7)
            run_literature_llm_operations
            exit_code=$?
            ;;
        8)
            # Exit
            return 0
            ;;
        9)
            run_test_suite
            exit_code=$?
            ;;
        *)
            log_error "Invalid option: $choice"
            log_info "Please enter a number between 0 and 9"
            exit_code=1
            ;;
    esac
    
    end_time=$(date +%s)
    duration=$(get_elapsed_time "$start_time" "$end_time")
    
    echo
    log_info "Operation completed in $(format_duration "$duration")"
    return $exit_code
}

# Run a sequence of menu options in order, stopping on first failure.
run_option_sequence() {
    local -a options=("$@")
    local exit_code=0

    if [[ ${#options[@]} -gt 0 ]]; then
        log_info "Running sequence: ${options[*]}"
    fi

    for opt in "${options[@]}"; do
        handle_menu_choice "$opt"
        exit_code=$?
        if [[ $exit_code -ne 0 ]]; then
            log_error "Sequence aborted at option $opt (exit code $exit_code)"
            return $exit_code
        fi
    done

    return $exit_code
}

# ============================================================================
# Non-Interactive Mode
# ============================================================================

run_non_interactive() {
    local option="$1"
    
    log_header "NON-INTERACTIVE MODE"

    if parse_choice_sequence "$option" && [[ ${#SHORTHAND_CHOICES[@]} -gt 1 ]]; then
        log_info "Running shorthand sequence: ${SHORTHAND_CHOICES[*]}"
        run_option_sequence "${SHORTHAND_CHOICES[@]}"
        exit $?
    fi

    log_info "Running option: $option"
    handle_menu_choice "$option"
    exit $?
}

# ============================================================================
# Help
# ============================================================================

show_help() {
    echo "Usage: $0 [OPTIONS]"
    echo
    echo "Literature Operations Orchestrator"
    echo
    echo "Options:"
    echo "  --help, -h          Show this help message"
    echo
    echo "Literature Operations:"
    echo "  --search            Search literature (network only, add to bibliography)"
    echo "  --download          Download PDFs (network only, for bibliography entries)"
    echo "  --extract-text       Extract text from PDFs (local only, save to extracted_text/)"
    echo "  --summarize         Generate summaries (requires Ollama, for papers with PDFs)"
    echo "  --cleanup            Cleanup library (local files only, remove papers without PDFs)"
    echo "  --llm-operation      Advanced LLM operations (requires Ollama)"
    echo "  --test               Run test suite (with coverage analysis)"
    echo
    echo "Main Menu Options (0-9):"
    echo
    echo "Orchestrated Pipelines:"
    echo "  0  Full Pipeline (search + download + extract + summarize)"
    echo "  1  Meta-Analysis Pipeline (search + download + extract + meta-analysis)"
    echo
    echo "Individual Operations:"
    echo "  2  Search Only (network only - add to bibliography)"
    echo "  3  Download Only (network only - download PDFs)"
    echo "  4  Extract Text (local only - extract text from PDFs)"
    echo "  5  Summarize (requires Ollama - generate summaries)"
    echo "  6  Cleanup (local files only - remove papers without PDFs)"
    echo "  7  Advanced LLM Operations (requires Ollama)"
    echo
    echo "Testing:"
    echo "  9  Run Test Suite (with coverage analysis)"
    echo
    echo "  8  Exit"
    echo
    echo "Examples:"
    echo "  $0                      # Interactive menu mode"
    echo "  $0 --search              # Search literature (add to bibliography)"
    echo "  $0 --download            # Download PDFs (for bibliography entries)"
    echo "  $0 --extract-text        # Extract text from PDFs"
    echo "  $0 --summarize           # Generate summaries (for papers with PDFs)"
    echo "  $0 --cleanup             # Cleanup library (remove papers without PDFs)"
    echo "  $0 --test                # Run test suite (with coverage analysis)"
    echo
}

# ============================================================================
# Main Entry Point
# ============================================================================

main() {
    # Parse command line arguments
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --help|-h)
                show_help
                exit 0
                ;;
            --option)
                if [[ -z "${2:-}" ]]; then
                    log_error "Missing option number"
                    show_help
                    exit 1
                fi
                run_non_interactive "$2"
                exit $?
                ;;
            --search)
                run_literature_search
                exit $?
                ;;
            --download)
                run_literature_download
                exit $?
                ;;
            --extract-text)
                run_literature_extract_text
                exit $?
                ;;
            --summarize)
                run_literature_summarize
                exit $?
                ;;
            --cleanup)
                run_literature_cleanup
                exit $?
                ;;
            --llm-operation)
                run_literature_llm_operations
                exit $?
                ;;
            --test)
                run_test_suite
                exit $?
                ;;
            *)
                log_error "Unknown option: $1"
                show_help
                exit 1
                ;;
        esac
        shift
    done
    
    # Interactive menu mode
    while true; do
        display_menu
        
        echo -n "Select option [0-9]: "
        read -r choice

        local exit_code=0
        if parse_choice_sequence "$choice" && [[ ${#SHORTHAND_CHOICES[@]} -gt 1 ]]; then
            run_option_sequence "${SHORTHAND_CHOICES[@]}"
            exit_code=$?
        else
            handle_menu_choice "$choice"
            exit_code=$?
        fi

        if [[ $exit_code -ne 0 ]]; then
            log_error "Last operation exited with code $exit_code"
        fi

        # Exit if choice is 8
        if [[ "$choice" == "8" ]]; then
            break
        fi

        # Don't prompt for cleanup option
        if [[ "$choice" != "6" ]]; then
            press_enter_to_continue
        fi
    done
}

# Run main
main "$@"


