import json
import pandas as pd
from utils import extract_features, score_wallet

# Load JSON file
with open("user-wallet-transactions.json") as f:
    data = json.load(f)

# Flatten and normalize records
records = []
for entry in data:
    records.append({
        "wallet": entry["userWallet"],
        "action": entry["action"],
        "timestamp": entry["timestamp"],
        "amount": float(entry.get("actionData", {}).get("amount", "0")) / 1e6,  # Assuming USDC-like decimals
        "assetPriceUSD": float(entry.get("actionData", {}).get("assetPriceUSD", "0"))
    })

df = pd.DataFrame(records)

# Group by wallet
wallet_groups = df.groupby("wallet")

results = []

for wallet, group in wallet_groups:
    features = extract_features(group)
    score = score_wallet(features)
    results.append({
        "wallet": wallet,
        **features,
        "score": score
    })

results_df = pd.DataFrame(results)
results_df.to_csv("wallet_scores.csv", index=False)

print("✅ Wallet scores saved to wallet_scores.csv")
