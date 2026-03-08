from __future__ import annotations

from pathlib import Path


def write_modelfile(output_dir: Path, model_name: str, gguf_filename: str) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    modelfile = output_dir / "Modelfile"
    modelfile.write_text(
        "\n".join(
            [
                f"FROM ./{gguf_filename}",
                'SYSTEM "You are an Agentic SOC Architect. Return strict JSON only."',
                "PARAMETER temperature 0.1",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    return modelfile


def export_commands(merged_model_dir: Path, gguf_out: Path) -> str:
    return "\n".join(
        [
            "# Convert HF model to GGUF (llama.cpp)",
            f"python convert_hf_to_gguf.py {merged_model_dir} --outfile {gguf_out} --outtype q4_k_m",
            "# Optional: higher quality quant",
            f"./quantize {gguf_out} {gguf_out.with_name(gguf_out.stem + '-q5_k_m.gguf')} q5_k_m",
        ]
    )
