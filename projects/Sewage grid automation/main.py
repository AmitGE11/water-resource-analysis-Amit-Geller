import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import os

def identify_necessary_manholes(pipes_dataframe):
    """
    Identifies necessary manholes based on connectivity and sampling rules.
    Returns a set of necessary manhole labels.
    """
    print("\n" + "="*50)
    print("IDENTIFYING MANHOLES TO DISPLAY")
    print("="*50)

    # Create a graph to understand the network structure
    G = nx.from_pandas_edgelist(pipes_dataframe, 'Start Node', 'Stop Node')
    print(f"Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

    if G.number_of_nodes() == 0:
        return set()

    # Step 1: Identify "critical" manholes (endpoints and intersections)
    necessary_mh = {node for node, degree in G.degree() if degree != 2}
    print(f"Found {len(necessary_mh)} critical manholes (intersections/endpoints).")

    # Step 2: Apply the "keep one, skip three" rule for long chains
    visited_chains = set()
    additional_mh = set()  # Store additional manholes to add later
    
    for node in necessary_mh:
        for neighbor in G.neighbors(node):
            if G.degree(neighbor) == 2 and tuple(sorted((node, neighbor))) not in visited_chains:
                chain = []
                prev, curr = node, neighbor
                while G.degree(curr) == 2:
                    chain.append(curr)
                    visited_chains.add(tuple(sorted((prev, curr))))
                    next_node_options = [n for n in G.neighbors(curr) if n != prev]
                    if not next_node_options: break
                    next_node = next_node_options[0]
                    prev, curr = curr, next_node
                visited_chains.add(tuple(sorted((prev, curr))))
                
                if chain:
                    for i, chain_node in enumerate(chain):
                        if i % 4 == 0:
                            additional_mh.add(chain_node)
    
    # Add the additional manholes to the necessary set
    necessary_mh.update(additional_mh)

    print(f"Total manholes to display after applying chain rule: {len(necessary_mh)}")
    return necessary_mh

def create_and_save_plot(title, filename, save_path, plot_pipes_df, plot_mh_df, all_mh_df):
    """
    Creates and saves a network plot.
    - Pipes are drawn from plot_pipes_df.
    - Manhole dots are drawn from plot_mh_df.
    - all_mh_df is used for coordinate lookups.
    """
    print(f"\nCreating plot: {title}...")
    mh_coords = {row['Label']: (row['X (m)'], row['Y (m)']) for _, row in all_mh_df.iterrows()}
    
    plt.figure(figsize=(20, 16))
    
    # Plot Pipes
    for _, pipe in plot_pipes_df.iterrows():
        start_node, stop_node = pipe['Start Node'], pipe['Stop Node']
        if start_node in mh_coords and stop_node in mh_coords:
            x1, y1 = mh_coords[start_node]
            x2, y2 = mh_coords[stop_node]
            plt.plot([x1, x2], [y1, y2], 'r-', linewidth=0.7, alpha=0.8)

    # Plot Manholes (the dots)
    mh_to_plot_labels = set(plot_mh_df['Label'])
    mh_x = [mh_coords[label][0] for label in mh_to_plot_labels if label in mh_coords]
    mh_y = [mh_coords[label][1] for label in mh_to_plot_labels if label in mh_coords]
    plt.scatter(mh_x, mh_y, c='darkred', s=1, zorder=5)

    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel('X Coordinate (m)', fontsize=12)
    plt.ylabel('Y Coordinate (m)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    stats_text = f'Total Pipes: {len(plot_pipes_df)}\nManholes Displayed: {len(plot_mh_df)}'
    plt.figtext(0.02, 0.02, stats_text, fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray", alpha=0.8))
    
    plt.tight_layout()
    
    full_path = os.path.join(save_path, filename)
    plt.savefig(full_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Successfully saved '{filename}'")

def main():
    """Main function to run the entire pipeline."""
    # --- CHANGE: Use os.path.join for robust file paths ---
    base_path = r"C:\Users\AmitGeller\Desktop\Yaron Geller\Grid_automation"
    pipes_path = os.path.join(base_path, "ofakim pipe data 01.csv")
    mh_path = os.path.join(base_path, "ofakim MH data 01.csv")

    pipes_df = pd.read_csv(pipes_path)
    mh_df = pd.read_csv(mh_path)

    print("Original DataFrames loaded successfully.")
    print(f"Pipes: {len(pipes_df)}, Manholes: {len(mh_df)}")

    # --- CHANGE 1: This is the primary logical fix. ---
    # The simplification is now purely for deciding which manholes to DISPLAY.
    # The pipe geometry is always taken from the original data.
    necessary_mh_labels = identify_necessary_manholes(pipes_df)
    simplified_mh_df = mh_df[mh_df['Label'].isin(necessary_mh_labels)].copy()

    # Save the original pipes data (with all columns)
    original_pipes_path = os.path.join(base_path, "original_pipes.csv")
    pipes_df.to_csv(original_pipes_path, index=False)
    print(f"Saved original pipes data to: {original_pipes_path}")
    
    # Save the list of simplified manholes
    simplified_mh_path = os.path.join(base_path, "simplified_manholes.csv")
    simplified_mh_df.to_csv(simplified_mh_path, index=False)
    print(f"Saved simplified manholes data to: {simplified_mh_path}")
    
    # Create simplified pipes data (filter pipes that connect to simplified manholes)
    simplified_pipes_df = pipes_df[
        (pipes_df['Start Node'].isin(necessary_mh_labels)) & 
        (pipes_df['Stop Node'].isin(necessary_mh_labels))
    ].copy()
    
    # Save the simplified pipes data (with all original columns)
    simplified_pipes_path = os.path.join(base_path, "simplified_pipes.csv")
    simplified_pipes_df.to_csv(simplified_pipes_path, index=False)
    print(f"Saved simplified pipes data to: {simplified_pipes_path}")

    # --- PLOTTING ---
    # Plot 1: Original Network (All pipes, all manholes)
    create_and_save_plot(
        title='ORIGINAL Sewage Pipe Network - Ofakim',
        filename='original_network.png',
        save_path=base_path,
        plot_pipes_df=pipes_df,
        plot_mh_df=mh_df,
        all_mh_df=mh_df
    )

    # Plot 2: Simplified Network (All pipes, selected manholes)
    create_and_save_plot(
        title='SIMPLIFIED Sewage Pipe Network - Ofakim',
        filename='simplified_network.png',
        save_path=base_path,
        plot_pipes_df=pipes_df, # IMPORTANT: We use the ORIGINAL pipes for geometry
        plot_mh_df=simplified_mh_df, # But the SIMPLIFIED manholes for dots
        all_mh_df=mh_df
    )
    
    print("\n" + "="*50)
    print("PROCESSING COMPLETE")
    print("="*50)

# --- CHANGE: Use a main execution block ---
if __name__ == "__main__":
    main()