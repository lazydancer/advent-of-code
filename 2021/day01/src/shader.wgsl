[[block]]
struct PrimeIndices {
    data: [[stride(4)]] array<u32>;
}; // this is used as both input and output for convenience

[[group(0), binding(0)]]
var<storage, read> v_indices: PrimeIndices;
[[group(0), binding(1)]]
var<storage, write> output: PrimeIndices;


fn increase(index: u32) -> u32 {
    if (index == 0u) {
        return 0u;
    }

    if (v_indices.data[index] > v_indices.data[index - 1u]) {
        return 1u;
    }
    return 0u;
}

[[stage(compute), workgroup_size(1)]]
fn main([[builtin(global_invocation_id)]] global_id: vec3<u32>) {
    output.data[global_id.x] = increase(global_id.x);
}