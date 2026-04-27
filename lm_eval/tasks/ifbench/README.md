# IFBench

## Paper

Title: Generalizing Verifiable Instruction Following

Abstract: https://arxiv.org/abs/2507.02833

IFBench evaluates precise instruction following generalization on new,
verifiable output constraints. It extends the instruction-following evaluation
setting beyond the original IFEval constraints and reports strict and loose
prompt-level and instruction-level metrics.

Homepage: https://github.com/allenai/IFBench

### Citation

```text
@misc{pyatkin2025generalizing,
   title={Generalizing Verifiable Instruction Following},
   author={Valentina Pyatkin and Saumya Malik and Victoria Graf and Hamish Ivison and Shengyi Huang and Pradeep Dasigi and Nathan Lambert and Hannaneh Hajishirzi},
   year={2025},
   journal={Advances in Neural Information Processing Systems},
   volume={38},
   year={2025}
}
```

### Groups, Tags, and Tasks

#### Groups

* Not part of a group yet.

#### Tags

* Not part of a tag yet.

#### Tasks

* `ifbench`: IFBench metrics from the local IFBench test dataset; this is the base metric.
* `ifbench_ifbench-constraints_single-turn`: Single-turn `prompt` evaluation using the `ifbench_constraints` partition from `allenai/IFBench_multi-turn`.
* `ifbench_ifbench-constraints_multi-turn`: Multi-turn chat-format evaluation using the `ifbench_constraints` partition from `allenai/IFBench_multi-turn`.
* `ifbench_ifeval-constraints_single-turn`: Single-turn `prompt` evaluation using the `ifeval_constraints` partition from `allenai/IFBench_multi-turn`.
* `ifbench_ifeval-constraints_multi-turn`: Multi-turn chat-format evaluation using the `ifeval_constraints` partition from `allenai/IFBench_multi-turn`.

The local `ifbench` task uses `/iopsstor/scratch/cscs/jgarcagi/projects/IFBench/data/IFBench_test.jsonl`
and verifier logic copied from `/users/jgarcagi/iopsstor/projects/IFBench`.
Only `ifbench` is wired into the local offline EASD benchmark grid. The
multi-turn task configs follow the upstream task names from EleutherAI PR #3642
and still point at `allenai/IFBench_multi-turn`.

### Checklist

For adding novel benchmarks/datasets to the library:

* [x] Is the task an existing benchmark in the literature?
  * [x] Have you referenced the original paper that introduced the task?
  * [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?

If other tasks on this dataset are already supported:

* [x] Is the "Main" variant of this task clearly denoted?
* [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [x] Have you noted which, if any, published evaluation setups are matched by this variant?

### Changelog

* Local fork: added IFBench task configs and verifier logic for EASD benchmarking.
