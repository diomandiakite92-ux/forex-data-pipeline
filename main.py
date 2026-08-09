# ============================
# Forex Data Pipeline
# ============================


def display_configuration(config):
    print("---------------------------")
    print("Forex Data Pipeline")
    print("---------------------------")
    print(f"Pair       : {config['pair']}")
    print(f"Timeframe  : {config['timeframe']}")
    print(f"Candles    : {config['candles']}")


def validate_configuration(config):
    if config["candles"] > 0:
        print("Configuration is valid.")
    else:
        print("Error: The number of candles must be greater than zero.")


def main():

    #  configuration
    config = {
        "pair": "EUR/USD",
        "timeframe": "H1",
        "candles": 500
    }

    # appeler display_configuration()
    display_configuration(config)

    # appeler validate_configuration()
    validate_configuration(config)

    # tes paires
    pairs = [
        "EUR/USD",
        "GBP/USD",
        "USD/JPY",
        "AUD/USD",
        "USD/CAD"
    ]

    for pair in pairs:
        # afficher pair
        print(f"- {pair}")


if __name__ == "__main__":
    main()
