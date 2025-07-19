# Aave V2 Wallet Credit Scoring

This project uses DeFi transaction data from Aave V2 to assign a credit score (0-1000) to wallets based on their behavior.

## Features Used
- Count of actions: deposit, borrow, repay, liquidation, redeem
- Ratios like repay/borrow and liquidation ratio

## Scoring Logic
- Rewards for repayments, deposits
- Penalties for liquidation events
- Scaled and bounded between 0 and 1000

## How to Run
```bash
pip install -r requirements.txt
python main.py
