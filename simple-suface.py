import rhinoscriptsyntax as rs

def main():
    # Prompt the user to select surfaces
    surfaces = rs.GetObjects("Select surfaces to calculate", rs.filter.surface, preselect=True)

    if not surfaces:
        print("No surfaces selected.")
        return

    # Calculate the number of surfaces
    num_surfaces = len(surfaces)

    # Calculate the total surface area
    total_area = 0.0
    for surface in surfaces:
        area = rs.SurfaceArea(surface)
        if area:
            total_area += area[0]  # The first element of the result is the area

    # Convert the total area to square meters (assuming Rhino uses square millimeters)
    total_area_m2 = total_area / 1e6

    # Output the results
    print(f"Nr of surfaces: {num_surfaces}")
    print(f"Total area in m2: {total_area_m2:.2f} m2")

if __name__ == "__main__":
    main()
