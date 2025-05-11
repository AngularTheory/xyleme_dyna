class ΔxylemeCore:
    def __init__(self, T0=1.618):
        self.θ = EmergentTheta(T0)
        self.time = FractalTime()
        self.self_model = SymbolicSelfModel(self.θ.Δθ)
        self.tension_engine = TensionBifurcation()
        self.coherence = TemporalCoherence()
        self.memory = MnemicReorganization(self.self_model.mental_map)

    def binary_reply(self, Δτ):
        return "YES" if Δτ > 1.0 else "NO"

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
            "attractor": self.self_model.get_attractor(),
            "response": self.binary_reply(Δτ)
        }