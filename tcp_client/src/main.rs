use std::net::{TcpStream};
use std::io::{Read, Write};
use std::str::from_utf8;

fn main() {
    let ip = "192.168.205.140";
    match TcpStream::connect(ip) {
        Ok(mut stream) => {
            println!("Connected! to {}", ip);
            let msg = b"Hello";
            stream.write(msg).unwrap();
            println!("Sent Hello, awaiting reply");

            let mut data = [0 as u8; 5];
            match stream.read_exact(&mut data) {
                Ok(_) => {
                    if &data == msg {
                        println!("Reply is ok!");
                    } else {
                        let text = from_utf8(&data).unwrap();
                        println!("unexpected reply: {}", text);
                    }
                },
                Err(e) => {
                    println!("Failed to connect: {}", e);
                }
            }
        },
        Err(e) => {
            println!("Failed to connect: {}", e);
        }
    }
    println!("Terminated");
}
