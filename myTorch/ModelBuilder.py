import yaml

# Define a function to parse the YAML file and create the model
def create_model_from_yaml(yaml_file):
    with open(yaml_file, 'r') as file:
        config = yaml.safe_load(file)

    model_config = config['model']
    layers_config = model_config['layers']
    
    # Build the layers based on the config
    layers = []
    for layer in layers_config:
        for key, value in layer.items():
            if key == 'Input':
                input_size, output_size = value[0], value[0]
            elif key == 'Dense':
                input_size, output_size = output_size, value
                layers.append(f'Dense({input_size}, {output_size})')
            elif key == 'Act':
                if value == 'tanh':
                    layers.append('Tanh()')
                elif value == 'sigmoid':
                    layers.append('Sigmoid()')
            elif key == 'Dropout':
                layers.append(f'Dropout({value})')

    # Define loss
    loss = model_config['loss']
    if loss == 'binary_crossentropy':
        loss_function = 'BinaryCrossEntropy()'

    # Create model representation
    model = f'model = Model({layers}, {loss_function})'
    return model

# Example usage
yaml_file = 'model.yml'  # replace with your actual file path
model = create_model_from_yaml(yaml_file)
