mod years;

use std::env;

fn main() -> anyhow::Result<()> {
    let args: Vec<String> = env::args().collect();
    if args.len() < 3 {
        eprintln!("Usage: {} <year> <day>", args[0]);
        return Ok(());
    }

    let year: u32 = args[1].parse().expect("Invalid year");
    let day: u32 = args[2].parse().expect("Invalid day");

    years::run(year, day)
}
