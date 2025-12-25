use std::fs;
use std::path::Path;

const PER_YEAR_CODE: &str = r#"
use anyhow::Result;

{mods}

pub fn run(day: u32) -> Result<()> {
    match day {
{match_arms}
        _ => anyhow::bail!("Day {day} is not supported for Year {year}."),
    }
}
"#;
const SCRIPT_NAME: &str = "day.rs";

fn generate_year_code(year: u32) {
    let out = Path::new("src")
        .join("years")
        .join(format!("year{}.rs", year));

    let mut mods = String::new();
    let mut match_arms = String::new();

    for entry in fs::read_dir(year.to_string()).unwrap() {
        let entry = entry.unwrap();
        let file_type = entry.file_type().unwrap();
        let script = entry.path().join(SCRIPT_NAME);

        if file_type.is_dir() && script.exists() {
            let day = entry.file_name().into_string().unwrap();
            mods.push_str(&format!(
                "#[path = \"../../{year}/{day}/{SCRIPT_NAME}\"] mod day{day};\n"
            ));
            match_arms.push_str(&format!(
                "        {d} => day{day}::run(),\n",
                d = day.parse::<u32>().unwrap()
            ));
        }
    }

    let code = PER_YEAR_CODE
        .replace("{mods}", &mods)
        .replace("{match_arms}", &match_arms)
        .replace("{year}", &year.to_string());
    fs::write(out, code).unwrap();
}

fn main() {
    generate_year_code(2024);
}
