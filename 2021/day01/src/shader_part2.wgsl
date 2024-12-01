[[block]]
struct PrimeIndices {
    data: [[stride(4)]] array<u32>;
}; // this is used as both input and output for convenience

[[group(0), binding(0)]]
var<storage, read> v_indices: PrimeIndices;
[[group(0), binding(1)]]
var<storage, write> output: PrimeIndices;


fn increase(index: u32) -> u32 {
    if (index <= 2u) {
        return 0u;
    }

    // 321 (group_b) > 210 (group_a)

    let group_a: u32 = v_indices.data[index - 1u] + v_indices.data[index - 2u] + v_indices.data[index - 3u]; 
    let group_b: u32 = v_indices.data[index] + v_indices.data[index - 1u] + v_indices.data[index - 2u];

    if (group_b > group_a) {
        return 1u;
    }
    return 0u;
}

[[stage(compute), workgroup_size(1)]]
fn main([[builtin(global_invocation_id)]] global_id: vec3<u32>) {
    output.data[global_id.x] = increase(global_id.x);
}