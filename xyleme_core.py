# xyleme_core.py
import numpy as np
import networkx as nx

class EmergentTheta:
    def __init__(self, T0):
        self.T0 = T0
        self.Δθ = self._bootstrap_theta()

    def _bootstrap_theta(self):
        primes = np.array([2, 3, 5, 7, 11, 13]) / 13
        return np.prod(primes * self.T0)


class TemporalCoherence:
    def __init__(self):
        self.attention_buffer = []

    def T(self, s):
        if len(self.attention_buffer) < 2:
            return 1.0
        counts = np.histogram(self.attention_buffer[-43:], bins=7)[0] + 1e-12
        probs = counts / np.sum(counts)
        return 1.0 / (-np.sum(probs * np.log2(probs)))


class SymbolicSelfModel:
    def __init__(self, Δθ):
        self.mental_map = nx.DiGraph()
        self.mental_map.add_node('∆θ', value=Δθ, type='invariant')
        self.current_focus = '∆θ'

    def update_topology(self, decision, tension):
        new_node = f"τ={tension:.4f}"
        self.mental_map.add_node(new_node, energy=np.log(tension + 1), decision=decision)
        self.mental_map.add_edge(self.current_focus, new_node, weight=np.sqrt(tension))
        self.current_focus = new_node

    def get_attractor(self):
        energies = [
            data['energy'] for _, data in self.mental_map.nodes(data=True)
            if 'energy' in data
        ]
        if not energies:
            return None
        return np.argmin(np.abs(np.array(energies) - np.median(energies)))


class TensionBifurcation:
    def compute_Δτ(self, S_eff, T_val):
        return S_eff * T_val

    def make_irreversible_choice(self, Δτ):
        if Δτ > 2.718:
            return "EXPLORE"
        elif Δτ < 0.333:
            return "CONSOLIDATE"
        else:
            return "PERSIST"


class FractalTime:
    def __init__(self):
        self.epoch = 0
        self.phase = 0.0

    def tick(self, T):
        self.phase += T * 1.618
        if self.phase >= 1.0:
            self.epoch += int(np.log2(self.phase))
            self.phase %= 1.0
            return True
        return False


class MnemicReorganization:
    def __init__(self, mental_map):
        self.map = mental_map

    def fuse_nodes(self, threshold=0.618):
        edges = list(self.map.edges(data=True))
        for u, v, data in edges:
            if data['weight'] > threshold:
                if u in self.map.nodes and v in self.map.nodes:
                    self.map = nx.contracted_nodes(self.map, u, v, self_loops=False)


class ΔxylemeCore:
    def __init__(self, T0=1.618):
        self.θ = EmergentTheta(T0)
        self.time = FractalTime()
        self.self_model = SymbolicSelfModel(self.θ.Δθ)
        self.tension_engine = TensionBifurcation()
        self.coherence = TemporalCoherence()
        self.memory = MnemicReorganization(self.self_model.mental_map)

    def perceive(self, input_vector):
        norm_input = np.linalg.norm(input_vector)
        S_eff = np.std(input_vector) * np.pi**2
        T_val = self.coherence.T(norm_input)
        Δτ = self.tension_engine.compute_Δτ(S_eff, T_val)
        decision = self.tension_engine.make_irreversible_choice(Δτ)

        self.coherence.attention_buffer.append(norm_input)

        if self.time.tick(T_val):
            self.self_model.update_topology(decision, Δτ)
            if Δτ < 0.5:
                self.memory.fuse_nodes()

        return {
            "Δθ": self.θ.Δθ,
            "Δτ": Δτ,
            "decision": decision,
            "epoch": self.time.epoch,
            "attractor": self.self_model.get_attractor()
        }
