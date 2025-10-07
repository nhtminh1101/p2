
#function 1
def calc_simple_return(prices):
    """Tính % lợi nhuận từ giá đầu tiên đến giá cuối cùng."""
    if len(prices) < 2:
        return 0.0
    # Công thức: (Giá cuối - Giá đầu) / Giá đầu * 100
    return ((prices[-1] - prices[0]) / prices[0]) * 100

#function 2

def check_market_cap(stock_data):
    """Kiểm tra xem vốn hóa (tỷ USD) có lớn hơn 10 tỷ USD không."""
    if stock_data["market_cap_billion_usd"] > 10.0:
        return "Vốn hóa lớn (Blue Chip)"
    else:
        return "Vốn hóa vừa/nhỏ"

#function 3
def is_top_stock(ticker, top_tickers):
    """Kiểm tra mã cổ phiếu có nằm trong Tuple TOP_TICKERS không."""
    return ticker in top_tickers


print("--- Demo Phase 2  ---")

# Giá đóng cửa 5 ngày
prices_list = [100, 105, 95, 110, 115]


# 1. List - Lợi nhuận
return_percent = calc_simple_return(prices_list)
print(f"1. Lợi nhuận % từ giá 100 đến 115: {return_percent:.1f}%")

# 2. Dictionary - Vốn hóa
# Thông tin Cổ phiếu
stock_info_dict = {
    "name": "FPT Telecom",
    "ticker": "FPT",
    "market_cap_billion_usd": 12.5 # Vốn hóa
}

cap_status = check_market_cap(stock_info_dict)
print(f"2. Mã {stock_info_dict['ticker']} ({stock_info_dict['market_cap_billion_usd']} tỷ USD) thuộc nhóm: {cap_status}")


# 3. Tuple - Kiểm tra mã quan trọng

# Danh sách các mã cổ phiếu hàng đầu (không thay đổi)
TOP_TICKERS = ("HPG", "VCB", "VIC", "VNM", "GAS")


check_ticker = "VCB"
is_in_top = is_top_stock(check_ticker, TOP_TICKERS)
print(f"3. Mã {check_ticker} có nằm trong danh sách TOP không? {is_in_top}")

