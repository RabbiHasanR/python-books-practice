def print_models(unprinted_desing, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_desing:
        current_design = unprinted_desing.pop()

        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# Start with some designs that need to be printed.
unprinted_desing = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_desing[:], completed_models)
show_completed_models(completed_models)
print(unprinted_desing)
