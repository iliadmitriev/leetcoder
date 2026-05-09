
import (
	"slices"
	"strconv"
	"strings"
)

type (
	EventType int
)

const (
	MentionTypeAll  = "ALL"
	MentionTypeHere = "HERE"
	MentionTypeUser = "USER"

	Message = "MESSAGE"
	Offline = "OFFLINE"

	OfflinePeriod = 60
)

const (
	EventOffline EventType = iota
	EventMessage
)

type Event struct {
	evType    EventType
	timestamp int
	users     []int
	mention   string
}

// extractUserIDs split and extract user IDs from mentions with format like:
// "id1 id2 id3 id234" -> [1, 2, 3, 234]
func extractUserIDs(mentions string, cutID bool) []int {
	ids := make([]int, 0)

	for _, id := range strings.Split(mentions, " ") {
		if cutID {
			id = id[2:]
		}

		i, _ := strconv.Atoi(id)
		ids = append(ids, i)
	}

	return ids
}

func countMentions(numberOfUsers int, events [][]string) []int {
	eventsList := make([]Event, 0, len(events))
	userMentions := make([]int, numberOfUsers)
	userOffline := make([]int, numberOfUsers)

	for _, event := range events {
		evType := EventType(0)
		switch event[0] {
		case Message:
			evType = EventMessage
		case Offline:
			evType = EventOffline
		}

		timestamp, _ := strconv.Atoi(event[1])

		users := make([]int, 0)
		mention := ""

		if evType == EventMessage {
			switch event[2] {
			case MentionTypeAll:
				evType = EventMessage
				mention = MentionTypeAll
			case MentionTypeHere:
				evType = EventMessage
				mention = MentionTypeHere
			default:
				evType = EventMessage
				users = extractUserIDs(event[2], true)
				mention = MentionTypeUser
			}
		} else {
			users = extractUserIDs(event[2], false)
		}

		eventsList = append(eventsList, Event{
			evType:    evType,
			timestamp: timestamp,
			users:     users,
			mention:   mention,
		})
	}

	slices.SortFunc(eventsList, func(a, b Event) int {
		if a.timestamp != b.timestamp {
			return a.timestamp - b.timestamp
		}

		return int(a.evType) - int(b.evType)
	})

	for _, event := range eventsList {
		switch event.evType {
		case EventMessage:

			switch event.mention {
			case MentionTypeAll:
				for i := range numberOfUsers {
					userMentions[i]++
				}
			case MentionTypeHere:
				for i := range numberOfUsers {
					if userOffline[i] <= event.timestamp {
						userMentions[i]++
					}
				}
			default:
				for _, users := range event.users {
					userMentions[users]++
				}
			}

		case EventOffline:
			for _, user := range event.users {
				userOffline[user] = event.timestamp + OfflinePeriod
			}
		}
	}

	return userMentions
}
