from graphviz import Digraph
import os
import tempfile

# Define expanded example firewall rules with misconfigurations
firewall_rules = [
    {'protocol': 'tcp', 'src': '140.192.37.20', 's_port': 'any', 'dst': '0.0.0.0/0', 'd_port': '80', 'action': 'deny', 'type': 'normal'},
    {'protocol': 'tcp', 'src': '140.192.37.0/24', 's_port': 'any', 'dst': '0.0.0.0/0', 'd_port': '80', 'action': 'accept', 'type': 'generalization'},
    {'protocol': 'tcp', 'src': '0.0.0.0/0', 's_port': 'any', 'dst': '161.120.33.40', 'd_port': '80', 'action': 'accept', 'type': 'normal'},
    {'protocol': 'tcp', 'src': '140.192.37.0/24', 's_port': 'any', 'dst': '161.120.33.40', 'd_port': '80', 'action': 'deny', 'type': 'shadowing'},
    {'protocol': 'tcp', 'src': '140.192.37.30', 's_port': 'any', 'dst': '0.0.0.0/0', 'd_port': '21', 'action': 'deny', 'type': 'normal'},
    {'protocol': 'tcp', 'src': '140.192.37.0/24', 's_port': 'any', 'dst': '0.0.0.0/0', 'd_port': '21', 'action': 'accept', 'type': 'generalization'},
    {'protocol': 'tcp', 'src': '140.192.37.0/24', 's_port': 'any', 'dst': '161.120.33.40', 'd_port': '21', 'action': 'accept', 'type': 'normal'},
    {'protocol': 'tcp', 'src': '0.0.0.0/0', 's_port': 'any', 'dst': '0.0.0.0/0', 'd_port': 'any', 'action': 'deny', 'type': 'normal'},
    {'protocol': 'udp', 'src': '140.192.37.0/24', 's_port': 'any', 'dst': '161.120.33.40', 'd_port': '53', 'action': 'accept', 'type': 'normal'},
    {'protocol': 'udp', 'src': '0.0.0.0/0', 's_port': 'any', 'dst': '161.120.33.40', 'd_port': '53', 'action': 'accept', 'type': 'redundancy'},
    {'protocol': 'udp', 'src': '140.192.38.0/24', 's_port': 'any', 'dst': '161.120.35.0/24', 'd_port': 'any', 'action': 'accept', 'type': 'normal'},
    {'protocol': 'udp', 'src': '0.0.0.0/0', 's_port': 'any', 'dst': '0.0.0.0/0', 'd_port': 'any', 'action': 'deny', 'type': 'normal'},
    {'protocol': 'ip', 'src': '0.0.0.0/0', 's_port': 'any', 'dst': '0.0.0.0/0', 'd_port': 'any', 'action': 'deny', 'type': 'normal'},
]


def visualize_firewall_rules(rules):
    dot = Digraph(comment='Firewall Rules')

    # Increase the size of the graph area
    dot.attr(size='1000,100')

    for rule in rules:
        src = rule['src']
        dst = rule['dst']
        protocol = rule['protocol']
        s_port = rule['s_port']
        d_port = rule['d_port']
        action = rule['action']
        r_type = rule['type']

        # Add nodes for source and destination
        dot.node(src, src)
        dot.node(dst, dst)

        # Define edge style based on action
        edge_style = 'solid' if action == 'accept' else 'dashed'
        edge_color = 'green' if action == 'accept' else 'red'

        # Highlight misconfigurations with specific colors
        if r_type == 'shadowing':
            edge_color = 'blue'
        elif r_type == 'correlation':
            edge_color = 'orange'
        elif r_type == 'redundancy':
            edge_color = 'purple'
        elif r_type == 'generalization':
            edge_color = 'brown'
        
        # Add edge with details
        edge_label = f"{protocol.upper()} {s_port}->{d_port} {action.upper()} ({r_type.upper()})"
        dot.edge(src, dst, label=edge_label, style=edge_style, color=edge_color)

    return dot

# Create the graph
dot = visualize_firewall_rules(firewall_rules)

# Define a known directory with write permissions
output_dir = os.path.expanduser('~')
filename = os.path.join(output_dir, 'firewall_rules_misconfigurations_graph')

try:
    # Render the graph to a PDF file directly
    dot.format = 'pdf'
    dot.render(filename)
    
    # View the rendered PDF file
    os.startfile(filename + '.pdf')
except Exception as e:
    print(f"An error occurred: {e}")

# To display in a Jupyter notebook, uncomment the following line:
# from IPython.display import Image, display
# display(Image(filename=f'{filename}.pdf'))
