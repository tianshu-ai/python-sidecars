#!/usr/bin/env python3
"""Download the Clef-flash model from ModelScope (fastest in China) or HuggingFace."""

import argparse
import os


def main():
    parser = argparse.ArgumentParser(description="Download Clef model")
    parser.add_argument("--model", default="clef-flash", choices=["clef-flash", "clef", "laya"],
                        help="Model to download (default: clef-flash)")
    parser.add_argument("--source", default="modelscope", choices=["modelscope", "huggingface"],
                        help="Download source (default: modelscope, faster in China)")
    parser.add_argument("--output", default="./models",
                        help="Output directory (default: ./models)")
    args = parser.parse_args()

    model_map = {
        "clef-flash": "Cloudflare/clef-flash",
        "clef": "Cloudflare/clef",
        "laya": "convaiinnovations/laya",
    }
    repo_id = model_map[args.model]

    print(f"Downloading {repo_id} from {args.source}...")

    if args.source == "modelscope":
        from modelscope import snapshot_download
        path = snapshot_download(repo_id, cache_dir=args.output)
    else:
        from huggingface_hub import snapshot_download
        hf_endpoint = os.environ.get("HF_ENDPOINT", "")
        kwargs = {"local_dir": os.path.join(args.output, args.model)}
        if hf_endpoint:
            print(f"Using HF mirror: {hf_endpoint}")
        path = snapshot_download(repo_id, **kwargs)

    print(f"Downloaded to: {path}")


if __name__ == "__main__":
    main()
