use aoc_core::{Input, Task};
use regex::Regex;
use std::io::BufRead;

#[derive(Debug)]
struct Data {
    memory: String,
}

fn parse_input(reader: &mut dyn BufRead) -> Data {
    let mut memory = String::new();
    reader.read_to_string(&mut memory).unwrap();
    Data { memory }
}

fn solve_one(data: &Data) -> String {
    let re = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();

    re.find_iter(&data.memory)
        .map(|mat| {
            let caps = re.captures(mat.as_str()).unwrap();
            let a: i32 = caps[1].parse().unwrap();
            let b: i32 = caps[2].parse().unwrap();
            a * b
        })
        .sum::<i32>()
        .to_string()
}

fn solve_two(data: &Data) -> String {
    let re = Regex::new(r"mul\((\d+),(\d+)\)|(don\'t)|(do)").unwrap();
    let mut doit = true;

    re.find_iter(&data.memory)
        .map(|mat| {
            let caps = re.captures(mat.as_str()).unwrap();
            if caps.get(3).is_some() {
                doit = false;
                0
            } else if caps.get(4).is_some() {
                doit = true;
                0
            } else if doit {
                let a: i32 = caps[1].parse().unwrap();
                let b: i32 = caps[2].parse().unwrap();
                a * b
            } else {
                0
            }
        })
        .sum::<i32>()
        .to_string()
}

const TASKS: [Task; 3] = [
    Task {
        name: "test1",
        input: Input::File("2024/03/test1.txt"),
        expected_one: Some("161"),
        expected_two: None,
    },
    Task {
        name: "test2",
        input: Input::File("2024/03/test2.txt"),
        expected_one: None,
        expected_two: Some("48"),
    },
    Task {
        name: "input",
        input: Input::File("2024/03/input.txt"),
        expected_one: Some("174561379"),
        expected_two: Some("106921067"),
    },
];

pub fn run() -> anyhow::Result<()> {
    aoc_core::run(&TASKS, parse_input, solve_one, solve_two);
    Ok(())
}
