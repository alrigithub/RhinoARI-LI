import Rhino
import scriptcontext as sc
import rhinoscriptsyntax as rs

def get_all_parent_layers(layer):
    """Get all parent layers of a given layer."""
    parents = []
    while layer and layer.ParentLayerId != Rhino.Geometry.Guid.Empty:
        parent_layer = next((l for l in sc.doc.Layers if l.Id == layer.ParentLayerId), None)
        if parent_layer:
            parents.append(parent_layer.Name)
            layer = parent_layer
        else:
            break
    return parents[::-1]  # Reverse to get top-down hierarchy

def get_unique_materials_with_layers():
    """Get all unique materials and the layers they are applied to, including parent layers."""
    materials_with_layers = {}

    for layer in sc.doc.Layers:
        material = layer.RenderMaterial
        if material is not None:
            if material.Name not in materials_with_layers:
                materials_with_layers[material.Name] = []

            parent_layers = get_all_parent_layers(layer)
            materials_with_layers[material.Name].append({
                "layer": layer.Name,
                "parent_layers": parent_layers
            })

    return materials_with_layers

def main():
    materials_with_layers = get_unique_materials_with_layers()

    if not materials_with_layers:
        print("No unique materials found.")
        return

    print("Unique materials with their associated layers and parent layers:")
    for material_name, layers in materials_with_layers.items():
        print(f"Material: {material_name}")
        for layer_info in layers:
            parent_info = " -> ".join(layer_info["parent_layers"]) if layer_info["parent_layers"] else "(No parent layers)"
            print(f"  Layer: {layer_info['layer']}, Parents: {parent_info}")

if __name__ == "__main__":
    main()
