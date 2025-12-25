use aoc_core::{Input, Task};
use std::{collections::HashMap, io::BufRead};

#[derive(Debug)]
struct Data {
    left: Vec<u32>,
    right: Vec<u32>,
}

fn parse_input(reader: &mut dyn BufRead) -> Data {
    let (left, right) = reader
        .lines()
        .map(|l| {
            let it = l.unwrap();
            let mut numbers = it.split_ascii_whitespace();
            let l: u32 = numbers.next().unwrap().parse().unwrap();
            let r: u32 = numbers.next().unwrap().parse().unwrap();
            (l, r)
        })
        .unzip();
    Data { left, right }
}

fn solve_one(data: &Data) -> String {
    let mut left = data.left.clone();
    let mut right = data.right.clone();
    left.sort_unstable();
    right.sort_unstable();

    let result: u32 = left
        .iter()
        .zip(right.iter())
        .map(|(l, r)| l.abs_diff(*r))
        .sum();

    result.to_string()
}

fn solve_two(data: &Data) -> String {
    let mut counter = HashMap::new();

    for &value in &data.right {
        *counter.entry(value).or_insert(0) += 1;
    }

    data.left
        .iter()
        .map(|&l| l * counter.get(&l).copied().unwrap_or(0))
        .sum::<u32>()
        .to_string()
}

const TASKS: [Task; 4] = [
    Task {
        name: "check 1",
        input: Input::Inline("1 3\n2 4\n"),
        expected_one: Some("4"), // 2 + 2,
        expected_two: Some("0"), // 1 * 0 + 2 * 0,
    },
    Task {
        name: "check 2",
        input: Input::Inline("1 1\n2 2\n"),
        expected_one: Some("0"), // 0 + 0,
        expected_two: Some("3"), // 1 * 1 + 2 * 1,
    },
    Task {
        name: "test",
        input: Input::File("2024/01/test.txt"),
        expected_one: Some("11"),
        expected_two: Some("31"),
    },
    Task {
        name: "input",
        input: Input::File("2024/01/input.txt"),
        expected_one: Some("3246517"),
        expected_two: Some("29379307"),
    },
];

pub fn run() -> anyhow::Result<()> {
    aoc_core::run(&TASKS, parse_input, solve_one, solve_two);
    Ok(())
}
