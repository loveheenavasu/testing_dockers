# checkout a new subscription for items

import chargebee
import json
chargebee.configure("live_ABetVcd08tNnxrFbwHv6FLPrHLMfeiBLS", "qricle")
result = chargebee.HostedPage.checkout_new_for_items({
    "subscription_items": [
        {
            "item_price_id": "1",
            "unit_price": 100
        }]
    })
hosted_page = result.hosted_page
