pub mod year2024;

pub fn run(year: u32, day: u32) -> anyhow::Result<()> {
    match year {
        2024 => year2024::run(day),
        _ => anyhow::bail!("Year {} is not supported yet.", year),
    }
}
