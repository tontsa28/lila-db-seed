import random
from modules.env import env
import modules.util as util


def update_puzzle_colls() -> None:
    args = env.args
    db = env.db
    
    if args.drop:
        db.puzzle2_round.drop()

    puzzles: list[PuzzleItem] = []

    for uid in env.uids:
        for _ in range(10):
            puzzle = random.choice(env.puzzles)
            pid = f"{uid}:{puzzle._id}"
            puzzles.append(PuzzleItem(uid, pid))

    if args.no_create:
        return
    
    util.bulk_write(db.puzzle2_round, puzzles)

class PuzzleItem:
    def __init__(self, uid: str, pid: str):
        self._id = pid
        self.w = random.choice([True, False])
        self.d = util.time_since_days_ago()
        self.u = uid