"""
Product Incubator - Diagram Generator

This script generates clean, professional diagrams in .drawio format
that can be opened and edited in diagrams.net (draw.io).

Usage:
    python generate_diagram.py --type system --output product_system.drawio
    python generate_diagram.py --type workflow --output product_workflow.drawio
"""

import argparse
import drawpyo


def create_system_diagram(output_path: str):
    """
    Creates a system architecture block diagram.
    Shows components and their connections.
    """
    file = drawpyo.File()
    file.file_path = output_path
    page = drawpyo.Page(file=file, name="System Architecture")
    
    # Create nodes
    input_node = drawpyo.diagram.Object(
        page=page, value="Input", 
        position=(50, 100), width=100, height=50
    )
    process_node = drawpyo.diagram.Object(
        page=page, value="Processing", 
        position=(200, 100), width=120, height=50
    )
    output_node = drawpyo.diagram.Object(
        page=page, value="Output", 
        position=(370, 100), width=100, height=50
    )
    
    # Create edges
    drawpyo.diagram.Edge(page=page, source=input_node, target=process_node)
    drawpyo.diagram.Edge(page=page, source=process_node, target=output_node)
    
    file.write()
    print(f"System diagram saved to {output_path}")


def create_workflow_diagram(output_path: str):
    """
    Creates a workflow/process flow diagram.
    Shows sequential steps in a process.
    """
    file = drawpyo.File()
    file.file_path = output_path
    page = drawpyo.Page(file=file, name="Workflow")
    
    # Define workflow steps
    steps = [
        "1. Conceptualize",
        "2. IP Check",
        "3. Technical Design",
        "4. Prototype",
        "5. Manufacture",
        "6. Legal/Business"
    ]
    
    nodes = []
    y_pos = 50
    for step in steps:
        node = drawpyo.diagram.Object(
            page=page, value=step,
            position=(100, y_pos), width=150, height=40
        )
        nodes.append(node)
        y_pos += 70
    
    # Connect nodes sequentially
    for i in range(len(nodes) - 1):
        drawpyo.diagram.Edge(page=page, source=nodes[i], target=nodes[i+1])
    
    file.write()
    print(f"Workflow diagram saved to {output_path}")


def create_electronics_diagram(output_path: str):
    """
    Creates an electronics block diagram.
    Shows microcontroller, motors, drivers, power, etc.
    """
    file = drawpyo.File()
    file.file_path = output_path
    page = drawpyo.Page(file=file, name="Electronics Block Diagram")
    
    # Power Supply
    power = drawpyo.diagram.Object(
        page=page, value="Power Supply\n12V DC",
        position=(50, 200), width=100, height=60
    )
    
    # Microcontroller
    mcu = drawpyo.diagram.Object(
        page=page, value="MCU\n(ESP32/Arduino)",
        position=(200, 150), width=120, height=80
    )
    
    # Motor Drivers
    driver1 = drawpyo.diagram.Object(
        page=page, value="Motor Driver 1",
        position=(380, 80), width=100, height=50
    )
    driver2 = drawpyo.diagram.Object(
        page=page, value="Motor Driver 2",
        position=(380, 220), width=100, height=50
    )
    
    # Motors
    motor1 = drawpyo.diagram.Object(
        page=page, value="Motor 1",
        position=(530, 80), width=80, height=50
    )
    motor2 = drawpyo.diagram.Object(
        page=page, value="Motor 2",
        position=(530, 220), width=80, height=50
    )
    
    # Sensor (optional)
    sensor = drawpyo.diagram.Object(
        page=page, value="Sensor",
        position=(200, 50), width=80, height=40
    )
    
    # Connections
    drawpyo.diagram.Edge(page=page, source=power, target=mcu)
    drawpyo.diagram.Edge(page=page, source=mcu, target=driver1)
    drawpyo.diagram.Edge(page=page, source=mcu, target=driver2)
    drawpyo.diagram.Edge(page=page, source=driver1, target=motor1)
    drawpyo.diagram.Edge(page=page, source=driver2, target=motor2)
    drawpyo.diagram.Edge(page=page, source=sensor, target=mcu)
    
    file.write()
    print(f"Electronics diagram saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate product diagrams in .drawio format")
    parser.add_argument(
        "--type", 
        choices=["system", "workflow", "electronics"],
        default="system",
        help="Type of diagram to generate"
    )
    parser.add_argument(
        "--output", 
        default="product_diagram.drawio",
        help="Output file path"
    )
    
    args = parser.parse_args()
    
    if args.type == "system":
        create_system_diagram(args.output)
    elif args.type == "workflow":
        create_workflow_diagram(args.output)
    elif args.type == "electronics":
        create_electronics_diagram(args.output)


if __name__ == "__main__":
    main()
