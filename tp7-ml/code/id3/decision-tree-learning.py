from collections import Counter
import math

from graphviz import Digraph

class Tree:
    def __init__(self, attribute):
        self.attribute = attribute
        self.branches = {}

    def addBranch(self, subtree, value):
        self.branches[value] = subtree

class Attribute:
    def __init__(self, values):
        self.values = values


def decisionTreeLearning (examples, attributes, parent_examples):
    if len(examples) == 0:
        return pluralityValue(parent_examples)
    elif sameClassification(examples):
        return examples[0][-1]
    elif len(attributes) == 0:
        return pluralityValue(examples)
    else:
        A = importance(attributes, examples)
        tree = Tree(A)
        for v in attributes[A].values:
            exs = [ex for ex in examples if ex[A] == v]
            attributes_copy = attributes.copy()
            del attributes_copy[A]
            subtree = decisionTreeLearning(exs, attributes_copy, examples)
            tree.addBranch(subtree, v)
        return tree


def sameClassification(examples):
    # Devuelve True si todos los ejemplos tienen la misma clasificación
    return len(set([ex[-1] for ex in examples])) == 1

def pluralityValue(examples):
    # Devuelve la clasificación más frecuente entre los ejemplos
    return Counter([ex[-1] for ex in examples]).most_common(1)[0][0]

def importance(attributes, examples):
    # Calcula la entropía antes de dividir
    entropy_before = calculate_entropy([ex[-1] for ex in examples])

    # Calcula la ganancia de información para cada atributo
    gains = {}
    for attribute in attributes:
        values = attributes[attribute].values
        entropy_after = 0
        for value in values:
            subset = [ex for ex in examples if ex[attribute] == value] # Subconjunto de ejemplos con el valor del atributo
            entropy_after += (len(subset) / len(examples)) * calculate_entropy([ex[-1] for ex in subset])
        gain = entropy_before - entropy_after
        gains[attribute] = gain

    # Devuelve el atributo con la mayor ganancia de información
    return max(gains, key=gains.get)


def calculate_entropy(labels):
    # Calcula la entropía de un conjunto de etiquetas
    label_counts = Counter(labels)
    entropy = 0
    for count in label_counts.values():
        probability = count / len(labels)
        entropy -= probability * math.log2(probability)
    return entropy


def visualize_decision_tree(tree, dot=None):
    if dot is None:
        dot = Digraph(comment='Decision Tree')

    if isinstance(tree, Tree):
        # Si el nodo es un objeto Tree
        if tree.attribute == 0:
            dot.node(str(id(tree)), f'Outlook')
        elif tree.attribute == 1:
            dot.node(str(id(tree)), f'Temperature')
        elif tree.attribute == 2:
            dot.node(str(id(tree)), f'Humidity')
        elif tree.attribute == 3:
            dot.node(str(id(tree)), f'Windy')
        for v, subtree in tree.branches.items():
            dot.node(str(id(subtree)), f'{v}')
            dot.edge(str(id(tree)), str(id(subtree)), label=v)
            visualize_decision_tree(subtree, dot)
    else:
        # Si el nodo es una clasificación
        dot.node(str(id(tree)), f'{tree}')

    return dot
    
def main():
    # Datos proporcionados
    data = [
        ['sunny', 'hot', 'high', 'false', 'no'],
        ['sunny', 'hot', 'high', 'true', 'no'],
        ['overcast', 'hot', 'high', 'false', 'yes'],
        ['rainy', 'mild', 'high', 'false', 'yes'],
        ['rainy', 'cool', 'normal', 'false', 'yes'],
        ['rainy', 'cool', 'normal', 'true', 'no'],
        ['overcast', 'cool', 'normal', 'true', 'yes'],
        ['sunny', 'mild', 'high', 'false', 'no'],
        ['sunny', 'cool', 'normal', 'false', 'yes'],
        ['rainy', 'mild', 'normal', 'false', 'yes'],
        ['sunny', 'mild', 'normal', 'true', 'yes'],
        ['overcast', 'mild', 'high', 'true', 'yes'],
        ['overcast', 'hot', 'normal', 'false', 'yes'],
        ['rainy', 'mild', 'high', 'true', 'no']
    ]

    # Atributos
    # 0: outlook, 1: temperature, 2: humidity, 3: windy
    attributes = {
        0: Attribute(['sunny', 'overcast', 'rainy']),
        1: Attribute(['hot', 'mild', 'cool']),
        2: Attribute(['high', 'normal']),
        3: Attribute(['false', 'true'])
    }


    # Clasificación: play
    parent_examples = []

    decision_tree = decisionTreeLearning(data, attributes, parent_examples)

    # Visualizar el árbol de decisión
    dot = visualize_decision_tree(decision_tree)
    dot.render('decision_tree', format='png', cleanup=True)


if __name__ == "__main__":
    main()