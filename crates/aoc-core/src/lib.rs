use std::fs::File;
use std::io::{BufRead, BufReader, Cursor};

#[derive(Debug)]
pub enum Input {
    File(&'static str),
    Inline(&'static str),
}

#[derive(Debug)]
pub struct Task {
    pub name: &'static str,
    pub input: Input,
    pub expected_one: Option<&'static str>,
    pub expected_two: Option<&'static str>,
}

pub fn run<T, PI, S1, S2>(tasks: &[Task], parse_input: PI, solve_one: S1, solve_two: S2)
where
    T: std::fmt::Debug,
    PI: Fn(&mut dyn BufRead) -> T,
    S1: Fn(&T) -> String,
    S2: Fn(&T) -> String,
{
    for task in tasks.iter() {
        println!("\n##### task: {} #####", task.name);
        let data = match task.input {
            Input::Inline(inline_str) => {
                let mut reader = Cursor::new(inline_str);
                parse_input(&mut reader)
            }
            Input::File(path) => {
                let file = File::open(path).unwrap();
                let mut reader = BufReader::new(file);
                parse_input(&mut reader)
            }
        };
        if task.name != "input" {
            println!("data={data:?}");
        }

        let start = std::time::Instant::now();
        let one = solve_one(&data);
        let end = std::time::Instant::now();
        let duration = end.duration_since(start);
        println!("one={one} (duration: {duration:?})");
        if let Some(expected) = &task.expected_one
            && one != *expected
        {
            println!("   UNEXPECTED RESULT! expected: {expected}");
        }

        let start = std::time::Instant::now();
        let two = solve_two(&data);
        let end = std::time::Instant::now();
        let duration = end.duration_since(start);
        println!("two={two} (duration: {duration:?})");
        if let Some(expected) = &task.expected_two
            && two != *expected
        {
            println!("   UNEXPECTED RESULT! expected: {expected}");
        }
    }
}
