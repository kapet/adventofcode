
use anyhow::Result;

#[path = "../../2024/01/day.rs"] mod day01;
#[path = "../../2024/02/day.rs"] mod day02;
#[path = "../../2024/03/day.rs"] mod day03;


pub fn run(day: u32) -> Result<()> {
    match day {
        1 => day01::run(),
        2 => day02::run(),
        3 => day03::run(),

        _ => anyhow::bail!("Day {day} is not supported for Year 2024."),
    }
}
