from pyvis.network import Network
import networkx as nx

# Create a networkx graph
G = nx.DiGraph()


nodes = [
    "Critique of Traditional Philosophy", "Will to Truth", "Dogmatism in Philosophy", "Value of Skepticism",
    "Philosophical Constructs as Expressions of Personality", "Free Spirit as a Challenger of Norms",
    "Revaluation of Values", "Independence and Intellectual Courage", "Self-Overcoming", 
    "Will to Power as a Driving Force", "Religious Instinct as a Psychological Phenomenon",
    "Critique of Ascetic Ideals", "Faith versus Knowledge", "The Role of Suffering in Religious Experience",
    "Transcendence and the Will to Power", "Morality as a Social Construct", "Master-Slave Morality",
    "The Origin of Guilt and Bad Conscience", "Psychological Basis of Morality", "Critique of Academic Scholarship",
    "The Problem of Objectivity", "The Role of the Philosopher vs. the Scholar", "Intellectual Mediocrity",
    "Scholarship as a Social Institution", "Reevaluation of Traditional Virtues", "Virtue as Self-Expression",
    "Virtue and Power", "Critique of Altruism", "Virtue and the Free Spirit", "Cultural Differences in Values",
    "Nationalism and Its Limitations", "The Influence of Environment on Thought", 
    "Interplay Between Individual and Collective", "European Identity and the Future", 
    "Aristocratic Values vs. Herd Morality", "Self-Mastery and Discipline", "Creative Power and Value Creation",
    "Loneliness and Distance as Noble Traits"
]

# Define the edges based on relationships
edges = [
    ("Will to Truth", "Critique of Traditional Philosophy"), 
    ("Value of Skepticism", "Will to Truth"), 
    ("Dogmatism in Philosophy", "Critique of Traditional Philosophy"),
    ("Philosophical Constructs as Expressions of Personality", "Critique of Traditional Philosophy"),
    ("Free Spirit as a Challenger of Norms", "Revaluation of Values"), 
    ("Independence and Intellectual Courage", "Free Spirit as a Challenger of Norms"),
    ("Self-Overcoming", "Revaluation of Values"), 
    ("Will to Power as a Driving Force", "Self-Overcoming"),
    ("Religious Instinct as a Psychological Phenomenon", "The Role of Suffering in Religious Experience"), 
    ("Critique of Ascetic Ideals", "Faith versus Knowledge"),
    ("Faith versus Knowledge", "Transcendence and the Will to Power"),
    ("The Role of Suffering in Religious Experience", "Critique of Ascetic Ideals"), 
    ("Morality as a Social Construct", "Master-Slave Morality"), 
    ("Psychological Basis of Morality", "The Complexity of Human Nature"), 
    ("The Problem of Objectivity", "Philosophical Constructs as Expressions of Personality"), 
    ("The Role of the Philosopher vs. the Scholar", "Revaluation of Values"), 
    ("Cultural Differences in Values", "Morality as a Social Construct"),
    ("Virtue and the Free Spirit", "Interplay Between Individual and Collective"), 
    ("Virtue and Power", "Will to Power as a Driving Force"),
    ("Aristocratic Values vs. Herd Morality", "Master-Slave Morality"),
    ("Self-Mastery and Discipline", "Self-Overcoming"), 
    ("Creative Power and Value Creation", "The Artist's Role in Revaluating Values"),
    ("Loneliness and Distance as Noble Traits", "Virtue and the Free Spirit")
]

G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Create a pyvis network
net = Network(notebook=True, cdn_resources='remote')
net.from_nx(G)

# Save and visualize the graph
net.show("nietzsche_map.html")
