from visualization.price_visualization import PriceVisualizer

viz = PriceVisualizer()

products_df = viz.load_products()
viz.plot_price_distribution(products_df)
viz.plot_top_expensive(products_df)

history_df = viz.load_price_history()
viz.plot_price_changes(history_df)
