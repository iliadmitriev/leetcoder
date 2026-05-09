
use std::cmp::Ordering;
use std::cmp::Ordering::Equal;
use std::iter::Iterator;
use std::string::String;
use std::vec::Vec;

#[derive(PartialEq, Eq, PartialOrd, Ord, Debug)]
enum EventType {
    Offline,
    Message,
}

#[derive(PartialEq, Eq, Debug)]
enum MentionType {
    All,
    Here,
    User,
}

const OFFLINE: &str = "OFFLINE";
const MESSAGE: &str = "MESSAGE";
const ALL: &str = "ALL";
const HERE: &str = "HERE";

const OFFLINE_PERIOD: i32 = 60;

#[derive(Debug)]
struct Event {
    event_type: EventType,
    mention_type: MentionType,
    timestamp: i32,
    users: Vec<i32>,
}

impl Solution {
    pub fn count_mentions(number_of_users: i32, events: Vec<Vec<String>>) -> Vec<i32> {
        let n = number_of_users as usize;
        let mut user_mentions = vec![0; n]; // number of mentions
        let mut user_offline = vec![0; n]; // number of seconds user offline

        // 1. convert events to struct
        // events: ["MESSAGE", "25", "ALL"], ["OFFLINE", "27", "3"], ["MESSAGE", "29", "HERE"],
        // ["MESSAGE", "30", "id1 id4 id8 id9"]
        // 2. sort events by timestamp and event_type
        // 3. calculate user_mentions

        let mut events = events
            .into_iter()
            .map(|event| {
                let timestamp = event[1].parse().unwrap();

                let event_type = match event[0].as_str() {
                    OFFLINE => EventType::Offline,
                    MESSAGE => EventType::Message,
                    _ => unreachable!(),
                };
                let mention_type = match event[2].as_str() {
                    ALL => MentionType::All,
                    HERE => MentionType::Here,
                    _ => MentionType::User,
                };

                let mut users: Vec<i32> = Vec::new();
                if event_type == EventType::Offline {
                    users = event[2]
                        .split_whitespace()
                        .filter_map(|user_id| user_id.parse().ok())
                        .collect();
                } else if mention_type == MentionType::User {
                    users = event[2]
                        .split_whitespace()
                        .filter_map(|user| {
                            user.strip_prefix("id")
                                .and_then(|user_id| user_id.parse().ok())
                        })
                        .collect();
                }

                Event {
                    event_type,
                    mention_type,
                    timestamp,
                    users,
                }
            })
            .collect::<Vec<_>>();

        events.sort_by(|a, b| {
            // sort by timestamp and then by event_type
            // if timestamp is the same, sort by event_type
            match a.timestamp.cmp(&b.timestamp) {
                std::cmp::Ordering::Equal => a.event_type.cmp(&b.event_type),
                ordering => ordering,
            }
        });

        events.iter().for_each(|event| match event.event_type {
            EventType::Offline => {
                event.users.iter().for_each(|&user_id| {
                    user_offline[user_id as usize] = event.timestamp + OFFLINE_PERIOD;
                });
            }
            EventType::Message => match event.mention_type {
                MentionType::All => {
                    user_mentions.iter_mut().for_each(|user_mentions| {
                        *user_mentions += 1;
                    });
                }
                MentionType::Here => {
                    for i in 0..n {
                        if user_offline[i] <= event.timestamp {
                            user_mentions[i] += 1;
                        }
                    }
                }
                MentionType::User => {
                    event.users.iter().for_each(|&user_id| {
                        user_mentions[user_id as usize] += 1;
                    });
                }
            },
        });

        return user_mentions;
    }
}