#!/usr/bin/env python3
"""
Simple test script to verify all Hugging Face endpoints are working
"""

import requests
import json
import time

BASE_URL = "http://127.0.0.1:8001"

def test_endpoint(endpoint, data, description):
    """Test a single endpoint"""
    print(f"\n🧪 Testing {description}...")
    try:
        response = requests.post(f"{BASE_URL}{endpoint}", json=data, timeout=30)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ SUCCESS: {description}")
            print(f"Response: {json.dumps(result, indent=2)[:200]}...")
            return True
        else:
            print(f"❌ FAILED: {description}")
            print(f"Status: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ ERROR: {description}")
        print(f"Error: {str(e)}")
        return False

def main():
    print("🚀 Testing Hugging Face Integration")
    print("=" * 50)
    
    # Test data
    test_text = """
    Good morning everyone. Today's meeting will cover our quarterly budget review.
    Sarah will present the financial analysis, showing we're currently 15% over budget.
    Mike suggested reducing marketing spend by 20% and reallocating funds to content marketing.
    Action items: Sarah to prepare budget reallocation plan by Friday.
    Mike to research content marketing agencies by next week.
    Meeting adjourned at 10:30 AM.
    """
    
    tests = [
        # Test split endpoint
        ("/split", {"text": test_text}, "Text Splitting"),
        
        # Test summarize endpoint
        ("/summarize", {"content": test_text}, "Meeting Summarization"),
        
        # Test upload endpoint
        ("/ingest/upload", {
            "title": "Test Quarterly Review", 
            "transcript": test_text
        }, "Meeting Upload"),
        
        # Test search endpoint (might fail if no data uploaded yet)
        ("/search", {"query": "budget review"}, "Meeting Search"),
    ]
    
    results = []
    for endpoint, data, description in tests:
        result = test_endpoint(endpoint, data, description)
        results.append(result)
        time.sleep(1)  # Small delay between tests
    
    print("\n" + "=" * 50)
    print("📊 Test Results Summary:")
    print(f"✅ Passed: {sum(results)}/{len(results)}")
    print(f"❌ Failed: {len(results) - sum(results)}/{len(results)}")
    
    if all(results):
        print("\n🎉 All tests passed! Your Hugging Face integration is working perfectly!")
    else:
        print("\n⚠️  Some tests failed. This is normal for the first run as models are downloading.")
        print("   Try running the tests again in a few minutes.")

if __name__ == "__main__":
    main()
