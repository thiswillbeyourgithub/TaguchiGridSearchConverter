from beartype import beartype
from typing import Dict, List, Any
from sklearn.model_selection import ParameterGrid
import numpy as np

@beartype  # this will apply to all methods
class TaguchiGridSearchConverter:
    __VERSION__: str = "0.0.1"

    def __init__(self) -> None:
        """
        Initializes a Taguchi Grid Search Converter.
        This class helps optimize hyperparameter search using Taguchi arrays.
        """
        pass

    def convert(self, param_grid: Dict[str, List[Any]]) -> List[Dict[str, Any]]:
        """
        Converts a full parameter grid into a reduced set using Taguchi array principles.
        
        Args:
            param_grid: Dictionary with parameters names (str) as keys and lists of
                       parameter settings to try as values.
        
        Returns:
            List of dictionaries with reduced parameter combinations to test.
        """
        # Get the number of parameters and their levels
        param_names = list(param_grid.keys())
        levels = [len(values) for values in param_grid.values()]
        
        # Determine the minimum number of experiments needed
        # Using the maximum number of levels as the base
        num_experiments = max(levels)
        
        # Create the reduced parameter combinations
        reduced_grid = []
        for i in range(num_experiments):
            combination = {}
            for param, values in param_grid.items():
                # Cycle through values using modulo to ensure we stay within bounds
                idx = i % len(values)
                combination[param] = values[idx]
            reduced_grid.append(combination)
            
        return reduced_grid
