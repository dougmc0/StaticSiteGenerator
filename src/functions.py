def split_nodes_delimiter(old_nodes, delimiter, text_type):
    out = []
    for node in old_nodes:
        if node.text_type == text_type:
            out += node.text.split(delimiter)
        else:
            out.append(node)
    return out
