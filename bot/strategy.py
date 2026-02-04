# def buy_signal(df):
#     last = df.iloc[-1]
#     prev = df.iloc[-2]

#     return (
#         prev.ema9 < prev.ema21 and
#         last.ema9 > last.ema21 and
#         40 < last.rsi < 60
#     )
def buy_signal(df):
    return True