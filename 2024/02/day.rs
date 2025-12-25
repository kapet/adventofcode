use aoc_core::{Input, Task};
use std::io::BufRead;

#[derive(Debug)]
struct Data {
    reports: Vec<Vec<u32>>,
}

fn parse_input(reader: &mut dyn BufRead) -> Data {
    let reports = reader
        .lines()
        .map(|l| {
            l.unwrap()
                .split_ascii_whitespace()
                .map(|t| t.parse::<u32>().unwrap())
                .collect()
        })
        .collect();
    Data { reports }
}

fn _check(report: &Vec<u32>) -> bool {
    let diffs: Vec<i32> = report
        .iter()
        .zip(report[1..].iter())
        .map(|(a, b)| (*b as i32) - (*a as i32))
        .collect();

    diffs.iter().all(|v| {
        let it = v.abs();
        it >= 1 && it <= 3
    }) && (diffs.iter().all(|v| *v > 0) || diffs.iter().all(|v| *v < 0))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_check() {
        assert!(_check(&vec![1, 2, 3, 4])); // forwards ok
        assert!(_check(&vec![4, 3, 2, 1])); // backwards ok
        assert!(!_check(&vec![1, 3, 2, 4])); // bad order
        assert!(!_check(&vec![1, 5, 6, 7])); // step too big
    }
}

fn solve_one(data: &Data) -> String {
    data.reports
        .iter()
        .filter(|r| _check(r))
        .count()
        .to_string()
}

fn solve_two(data: &Data) -> String {
    data.reports
        .iter()
        .filter(|r| {
            if _check(r) {
                return true;
            }
            for i in 0..r.len() {
                let mut new_vec = Vec::with_capacity(r.len() - 1);
                new_vec.extend_from_slice(&r[..i]);
                new_vec.extend_from_slice(&r[i + 1..]);
                if _check(&new_vec) {
                    return true;
                }
            }
            false
        })
        .count()
        .to_string()
}

const TASKS: [Task; 2] = [
    Task {
        name: "test",
        input: Input::File("2024/02/test.txt"),
        expected_one: Some("2"),
        expected_two: Some("4"),
    },
    Task {
        name: "input",
        input: Input::File("2024/02/input.txt"),
        expected_one: Some("252"),
        expected_two: Some("324"),
    },
];

pub fn run() -> anyhow::Result<()> {
    aoc_core::run(&TASKS, parse_input, solve_one, solve_two);
    Ok(())
}
