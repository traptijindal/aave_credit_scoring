def extract_features(df):
    action_counts = df["action"].value_counts().to_dict()
    deposit = action_counts.get("deposit", 0)
    borrow = action_counts.get("borrow", 0)
    repay = action_counts.get("repay", 0)
    redeem = action_counts.get("redeemunderlying", 0)
    liquidation = action_counts.get("liquidationcall", 0)

    total_tx = len(df)

    total_deposit_value = df[df["action"] == "deposit"]["amount"] * df[df["action"] == "deposit"]["assetPriceUSD"]
    total_borrow_value = df[df["action"] == "borrow"]["amount"] * df[df["action"] == "borrow"]["assetPriceUSD"]
    total_repay_value = df[df["action"] == "repay"]["amount"] * df[df["action"] == "repay"]["assetPriceUSD"]

    return {
        "total_tx": total_tx,
        "deposit_count": deposit,
        "borrow_count": borrow,
        "repay_count": repay,
        "redeem_count": redeem,
        "liquidation_count": liquidation,
        "repay_borrow_ratio": repay / borrow if borrow > 0 else 0,
        "liquidation_ratio": liquidation / total_tx if total_tx > 0 else 0,
        "total_deposit_usd": total_deposit_value.sum(),
        "total_borrow_usd": total_borrow_value.sum(),
        "total_repay_usd": total_repay_value.sum(),
    }

def score_wallet(f):
    score = 500

    score += f["deposit_count"] * 2
    score += f["repay_count"] * 3
    score += f["repay_borrow_ratio"] * 100
    score += f["total_repay_usd"] * 0.01

    score -= f["liquidation_count"] * 5
    score -= f["liquidation_ratio"] * 200

    score = max(0, min(1000, int(score)))
    return score
