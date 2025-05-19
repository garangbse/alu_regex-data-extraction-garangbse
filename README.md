# Regex Data Extraction Tool

## Project Overview
This project implements a versatile text data extraction tool using regular expressions (regex) in Python. The tool can identify and extract various data types from text content, including:

- Email addresses
- Phone numbers
- Credit card numbers
- Hashtags

## Features
- **Multi-format extraction**: Handles different formatting variations for each data type
- **Modular design**: Each extraction function is implemented separately for clarity and maintainability
- **Interactive mode**: Test with included sample text or input your own custom text
- **Comprehensive pattern matching**: Identifies both standard and edge cases

## Core Functions

### `extract_data(text, data_type)`
The main function that routes extraction requests to the appropriate specialized function based on data type.

### Data Type Extractors
- `extract_email_addresses(text)`: Captures valid email addresses following standard format
- `extract_phone_numbers(text)`: Identifies phone numbers in various formats (international, local, with different separators)
- `extract_credit_card_numbers(text)`: Extracts potential credit card numbers with 16 digits in groups of 4
- `extract_hashtags(text)`: Captures hashtags commonly used on social media

## Usage
The program includes:
1. A demonstration using sample text with multiple examples of each data type
2. An interactive mode where you can enter your own text for processing

## Edge Cases Handled
The regex patterns are designed to handle common variations in data formats:
- Different email domain structures
- Various phone number formatting (parentheses, spaces, dashes)
- Credit card numbers with different separators
- Hashtags with alphanumeric characters

## Getting Started
Run the script to see extraction in action with the sample text, then try your own examples using the interactive prompt.

