from ortools.sat.python import cp_model
import sys
import pandas as pd
import matplotlib.pyplot as plt
import os

def read_knapsack_dataset(file_path):
    """
    On extrait ici la capacité depuis la ligne "MAX_CAPACITY" et, dans la section DATA,
    le profit (2ème colonne) et le poids (3ème colonne).
    """
    with open(file_path, "r") as f:
        lines = f.readlines()

    capacity = None
    profits = []
    weights = []
    data_section = False

    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Détection de la section DATA
        if line.upper().startswith("DATA"):
            data_section = True
            continue

        # En dehors de DATA, récupérer la capacité
        if not data_section:
            if line.upper().startswith("MAX_CAPACITY:"):
                try:
                    capacity = int(line.split(":", 1)[1].strip())
                except ValueError:
                    capacity = float(line.split(":", 1)[1].strip())
        else:
            # Dans DATA, chaque ligne est "id profit weight"
            parts = line.split()
            if len(parts) >= 3:
                try:
                    profit = int(parts[1])
                    weight = int(parts[2])
                except ValueError:
                    profit = float(parts[1])
                    weight = float(parts[2])
                profits.append(profit)
                weights.append(weight)
    
    if capacity is None:
        raise Exception("Impossible de trouver la capacité (MAX_CAPACITY) dans le fichier.")
    return capacity, weights, profits

def solve_knapsack_cp(capacity, weights, profits):
    """
    Modélisation du problème du sac à dos en CP-SAT.
    
    Variables :
      - Pour chaque item i, x[i] est une variable binaire indiquant s'il est sélectionné.
    
    Contrainte :
      - La somme (x[i]*weights[i]) doit être <= capacity.
    
    Objectif :
      - Maximiser la somme (x[i]*profits[i]).
    
    Renvoie la valeur objective, la liste des indices des items sélectionnés et le solveur.
    """
    model = cp_model.CpModel()
    n = len(weights)
    x = [model.NewBoolVar(f"x_{i}") for i in range(n)]
    
    model.Add(sum(x[i] * weights[i] for i in range(n)) <= capacity)
    model.Maximize(sum(x[i] * profits[i] for i in range(n)))
    
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        selected_items = [i for i in range(n) if solver.Value(x[i]) == 1]
        total_profit = sum(profits[i] for i in selected_items)
        total_weight = sum(weights[i] for i in selected_items)
        print("Solution trouvée :")
        print("  - Items sélectionnés :", selected_items)
        print("  - Profit total :", total_profit)
        print("  - Poids total :", total_weight, "sur une capacité de", capacity)
        print("  - Objective value :", solver.ObjectiveValue())
        print("  - Temps de résolution (ms) :", solver.WallTime())
        return solver.ObjectiveValue(), selected_items, solver
    else:
        print("Aucune solution trouvée.")
        return None, None, solver

def export_results_excel(file_name, results_dict, output_dir):
    """
    Exporte les résultats contenus dans results_dict dans un fichier Excel
    dans le dossier output_dir.
    """
    df = pd.DataFrame([results_dict])
    excel_file = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}_results.xlsx")
    df.to_excel(excel_file, index=False)
    print(f"Résultats exportés dans {excel_file}")

def plot_results(file_name, results_dict, output_dir):
    """
    Génère un graphique récapitulatif (graphique en barres) avec :
      - Capacité
      - Poids total utilisé
      - Profit optimal
      - Nombre total d'items et nombre d'items sélectionnés
      - Temps de résolution en ms
    Le graphique est enregistré dans le dossier output_dir au format PNG.
    """
    labels = ["Capacité", "Poids utilisé", "Profit optimal", "Nb Items", "Nb sélectionnés", "Temps (ms)"]
    values = [results_dict["Capacité"], results_dict["Total_Weight"], results_dict["Profit_Optimal"],
              results_dict["Nb_Items"], results_dict["Nb_Selected"], results_dict["Temps_ms"]]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color="skyblue")
    plt.title(f"Résultats pour {file_name}")
    plt.ylabel("Valeur")
    plt.xticks(rotation=45)
    png_file = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}_results.png")
    plt.tight_layout()
    plt.savefig(png_file)
    plt.show()
    print(f"Graphique enregistré dans {png_file}")


def plot_results_3d(file_name, results_dict, output_dir):
    """
    Génère un graphique en 3D représentant par exemple :
      - Axe X : Capacité (la capacité du sac),
      - Axe Y : Profit optimal obtenu,
      - Axe Z : Temps de résolution (ms).
    
    Le graphique est ensuite sauvegardé dans le dossier output_dir.
    """
    # Création de la figure et de l'axe 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Extraction des valeurs depuis le dictionnaire de résultats
    x_val = results_dict["Capacité"]
    y_val = results_dict["Profit_Optimal"]
    z_val = results_dict["Temps_ms"]
    
    # Pour une visualisation simple, on place un point 3D avec ces valeurs
    ax.scatter([x_val], [y_val], [z_val], s=100, c='blue')
    
    # Étiquettes des axes
    ax.set_xlabel("Capacité")
    ax.set_ylabel("Profit Optimal")
    ax.set_zlabel("Temps (ms)")
    ax.set_title(f"Graphique 3D pour {file_name}")
    
    # Sauvegarde du graphique dans le dossier output_dir
    png_file = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}_results_3D.png")
    plt.tight_layout()
    plt.savefig(png_file)
    plt.show()
    print(f"Graphique 3D enregistré dans {png_file}")

def main():
    # Création automatique du dossier "ResultPL" s'il n'existe pas
    output_dir = "ResultPL"
    os.makedirs(output_dir, exist_ok=True)
    
    # Le chemin du fichier est passé en paramètre ou défini ici
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "Data/pi-13-1000-1000-001.kna"  # chemin par défaut
    
    try:
        capacity, weights, profits = read_knapsack_dataset(file_path)
    except Exception as e:
        print("Erreur lors de la lecture du dataset :", e)
        return

    nb_items = len(weights)
    print("Capacité du sac :", capacity)
    print("Nombre d'items :", nb_items)
    
    profit_opt, selected_items, solver = solve_knapsack_cp(capacity, weights, profits)
    
    if profit_opt is not None:
        total_weight = sum(weights[i] for i in selected_items)
        total_profit = sum(profits[i] for i in selected_items)
        temps_ms = solver.WallTime()
        nb_selected = len(selected_items)
        
        results = {
            "Fichier": os.path.basename(file_path),
            "Nb_Items": nb_items,
            "Capacité": capacity,
            "Profit_Optimal": profit_opt,
            "Total_Profit": total_profit,
            "Total_Weight": total_weight,
            "Nb_Selected": nb_selected,
            "Temps_ms": temps_ms
        }
        
        export_results_excel(os.path.basename(file_path), results, output_dir)
        plot_results(os.path.basename(file_path), results, output_dir)
        plot_results_3d(os.path.basename(file_path), results, output_dir)
    else:
        print("Aucune solution optimale n'a pu être obtenue.")

if __name__ == "__main__":
    main()
