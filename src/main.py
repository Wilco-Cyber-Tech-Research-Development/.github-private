"""
COSMICA ULTRA HYPER-AGI
main.py
============================================================

Primary application entry point for the Cosmica Ultra Hyper-AGI engine.

Upgraded to work with the Ultra Hyper‑AGI‑ASI architecture,
featuring Transformer‑XL neural core, hierarchical planning,
world model, metacognition, and self‑improvement.

Run:

    python main.py

Interactive mode:

    python main.py --interactive

Diagnostics:

    python main.py --status

Create a goal:

    python main.py --goal "Analyze incoming information"

============================================================
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import Any, Dict

# Import the new Ultra engine
from cosmica_ultra_hyper_agi import (
    UltraConfig,
    CosmicaUltraHyperAGI,
)


# ============================================================
# VERSION
# ============================================================

COSMICA_NAME = "COSMICA ULTRA"
COSMICA_VERSION = "Hyper-AGI-ASI Research Core 2.0.0"

BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "models"
MEMORY_DIR = BASE_DIR / "memory"
LOG_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"

MODEL_PATH = MODEL_DIR / "ultra_hyper_agi.keras"
MEMORY_PATH = MEMORY_DIR / "ultra_memory.json"


# ============================================================
# DIRECTORIES
# ============================================================

def create_directories() -> None:
    """
    Create the runtime directory structure.
    """
    directories = [
        MODEL_DIR,
        MEMORY_DIR,
        LOG_DIR,
        DATA_DIR,
    ]
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


# ============================================================
# LOGGING
# ============================================================

def configure_logging() -> None:
    """
    Configure application logging.
    """
    log_file = LOG_DIR / "cosmica_ultra.log"
    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s | "
            "COSMICA-ULTRA | "
            "%(levelname)s | "
            "%(message)s"
        ),
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_file, encoding="utf-8"),
        ],
    )


logger = logging.getLogger("COSMICA-ULTRA-MAIN")


# ============================================================
# CONFIGURATION (Ultra)
# ============================================================

def build_configuration() -> UltraConfig:
    """
    Construct the Ultra configuration.
    """
    return UltraConfig(
        sequence_length=64,
        feature_dimension=256,
        hidden_dimension=512,
        attention_heads=8,
        num_transformer_layers=4,
        feed_forward_dim=2048,
        output_dimension=128,
        learning_rate=1e-4,
        dropout=0.15,
        memory_path=str(MEMORY_PATH),
        model_path=str(MODEL_PATH),
        confidence_threshold=0.7,
        enable_self_improvement=True,
        improvement_interval=50,
    )


# ============================================================
# TOOL DEFINITIONS (unchanged but can be extended)
# ============================================================

def tool_system_status() -> Dict[str, Any]:
    return {
        "engine": COSMICA_NAME,
        "version": COSMICA_VERSION,
        "status": "operational",
        "timestamp": time.time(),
        "python": sys.version.split()[0],
    }


def tool_time() -> Dict[str, Any]:
    return {
        "unix": time.time(),
        "human": time.strftime("%Y-%m-%d %H:%M:%S"),
    }


def tool_list_files() -> Dict[str, Any]:
    files = []
    for path in BASE_DIR.rglob("*"):
        if path.is_file():
            try:
                relative = path.relative_to(BASE_DIR)
                files.append(str(relative))
            except ValueError:
                continue
    return {
        "count": len(files),
        "files": files[:500],
    }


# ============================================================
# ENGINE REGISTRATION
# ============================================================

def register_tools(cosmica: CosmicaUltraHyperAGI) -> None:
    """
    Register controlled tools with the cognitive engine.
    """
    cosmica.tools.register(
        name="system_status",
        description="Return Cosmica Ultra system status.",
        function=tool_system_status,
    )
    cosmica.tools.register(
        name="system_time",
        description="Return current system time.",
        function=tool_time,
    )
    cosmica.tools.register(
        name="list_files",
        description="List project files in read‑only mode.",
        function=tool_list_files,
    )
    logger.info("Tool registry initialized.")


# ============================================================
# ENGINE BOOT
# ============================================================

def boot_cosmica() -> CosmicaUltraHyperAGI:
    """
    Boot the complete Cosmica Ultra cognitive engine.
    """
    logger.info("==========================================")
    logger.info("Starting %s", COSMICA_NAME)
    logger.info("Version: %s", COSMICA_VERSION)
    logger.info("==========================================")

    create_directories()
    config = build_configuration()
    cosmica = CosmicaUltraHyperAGI(config=config)
    register_tools(cosmica)

    logger.info("Memory system initialized (with consolidation).")
    logger.info("Goal management (hierarchical) initialized.")
    logger.info("Hierarchical planning engine initialized.")
    logger.info("Transformer‑XL neural core initialized.")
    logger.info("World model initialized.")
    logger.info("Metacognitive module initialized.")
    logger.info("Self‑improvement loop active.")
    logger.info("Governance layer (constitutional) initialized.")
    logger.info("COSMICA ULTRA successfully booted.")
    return cosmica


# ============================================================
# STATUS (enhanced with new components)
# ============================================================

def show_status(cosmica: CosmicaUltraHyperAGI) -> None:
    """
    Display complete system status, including new modules.
    """
    # Gather memory stats
    memory_stats = {}
    for mtype, lst in cosmica.memory.memories.items():
        memory_stats[mtype] = len(lst)

    active_goals = cosmica.goal_manager.get_active_goals()
    status = {
        "engine": COSMICA_NAME,
        "version": COSMICA_VERSION,
        "status": "OPERATIONAL",
        "memory": memory_stats,
        "goals": {
            "total": len(cosmica.goal_manager.goals),
            "active": len(active_goals),
        },
        "tools": list(cosmica.tools.tools.keys()),
        "neural_core": {
            "type": "Transformer-XL",
            "layers": cosmica.config.num_transformer_layers,
            "parameters": cosmica.neural_core.count_params(),
        },
        "world_model": {
            "state_dim": cosmica.world_model.state_dim,
            "action_dim": cosmica.world_model.action_dim,
        },
        "self_improvement": {
            "enabled": cosmica.config.enable_self_improvement,
            "steps": cosmica.self_improvement.step_count,
        },
        "runtime": {
            "python": sys.version.split()[0],
            "platform": sys.platform,
        },
    }
    print(json.dumps(status, indent=4))


# ============================================================
# GOAL MODE (supports hierarchical decomposition)
# ============================================================

def create_goal(cosmica: CosmicaUltraHyperAGI, description: str) -> None:
    """
    Create and optionally decompose a new cognitive goal.
    """
    goal = cosmica.set_goal(description=description, priority=0.8)
    print()
    print("COSMICA GOAL CREATED")
    print("-" * 40)
    print(f"ID: {goal.goal_id}")
    print(f"Goal: {goal.description}")
    print(f"Priority: {goal.priority}")
    print(f"Status: {goal.status}")

    # Plan for the goal
    plan = cosmica.reason(goal)
    print()
    print("GENERATED PLAN")
    print("-" * 40)
    if plan.get("type") == "hierarchical":
        print("Hierarchical plan with sub‑goals:")
        for sub in plan.get("subplans", []):
            print(f"  - {sub.get('goal', '')}")
    else:
        for action in plan.get("candidate_actions", []):
            print(f"  - {action}")
        if plan.get("best_action"):
            print(f"Best action: {plan['best_action']}")


# ============================================================
# COGNITIVE CYCLE (enhanced output)
# ============================================================

def run_cognitive_cycle(cosmica: CosmicaUltraHyperAGI, observation: str) -> None:
    """
    Run one complete cognitive cycle with the Ultra engine.
    """
    result = cosmica.cognitive_cycle(observation)
    print()
    print("COSMICA ULTRA COGNITIVE CYCLE")
    print("=" * 60)
    # Pretty print the result, omitting large arrays
    clean_result = {
        "observation": result.get("observation"),
        "active_goal": result.get("active_goal"),
        "plan": result.get("plan"),
        "thought": result.get("thought"),
        "authorization": result.get("authorization"),
        "execution": result.get("execution"),
        "timestamp": result.get("timestamp"),
        "step": result.get("step"),
    }
    print(json.dumps(clean_result, indent=4, default=str))


# ============================================================
# INTERACTIVE MODE (extended with new commands)
# ============================================================

def interactive_mode(cosmica: CosmicaUltraHyperAGI) -> None:
    """
    Start interactive Cosmica Ultra console.

    Commands:
        status
        goals
        memory <query>
        goal <description>
        think <observation>
        cycle <observation>
        tools
        execute <tool>
        plan <goal_id>        # Show plan for a goal
        decompose <goal_id> <sub1>,<sub2>  # Decompose a goal
        worldmodel            # Show world model state
        reflect               # Trigger metacognitive reflection
        help
        exit
    """
    print()
    print("=" * 60)
    print(f"{COSMICA_NAME} {COSMICA_VERSION}")
    print("=" * 60)
    print("Interactive cognitive interface online.")
    print("Type 'help' for available commands.")

    while True:
        try:
            command = input("\nCOSMICA> ").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            print("Shutting down COSMICA Ultra.")
            break

        if not command:
            continue

        if command.lower() in {"exit", "quit", "shutdown"}:
            print("COSMICA Ultra shutdown requested.")
            break

        # ---- HELP ----
        if command.lower() == "help":
            print("""
Available commands:

    status
        Show engine status (including new modules).

    goals
        Show active goals (hierarchical).

    memory <query>
        Search memory (semantic retrieval).

    goal <description>
        Create a new goal (with planning).

    think <observation>
        Store an observation (perception).

    cycle <observation>
        Run complete cognitive cycle.

    tools
        List registered tools.

    execute <tool>
        Execute a registered read-only tool.

    plan <goal_id>
        Show the plan for a given goal ID.

    decompose <goal_id> <subgoal1>,<subgoal2>,...
        Decompose a goal into sub‑goals.

    worldmodel
        Display world model parameters.

    reflect
        Run metacognitive reflection and show suggestion.

    help
        Show this menu.

    exit
        Shut down Cosmica.
""")
            continue

        # ---- STATUS ----
        if command.lower() == "status":
            show_status(cosmica)
            continue

        # ---- GOALS ----
        if command.lower() == "goals":
            goals = cosmica.goal_manager.get_active_goals()
            if not goals:
                print("No active goals.")
            else:
                for goal in goals:
                    print(f"\nID: {goal.goal_id}")
                    print(f"Goal: {goal.description}")
                    print(f"Priority: {goal.priority}")
                    print(f"Status: {goal.status}")
                    if goal.subgoals:
                        print(f"Sub‑goals: {', '.join(goal.subgoals)}")
            continue

        # ---- MEMORY ----
        if command.lower().startswith("memory "):
            query = command[7:].strip()
            memories = cosmica.remember(query=query, limit=5)
            if not memories:
                print("No matching memories.")
            else:
                for mem in memories:
                    print()
                    print(f"[{mem.memory_type}] (importance: {mem.importance:.2f})")
                    print(mem.content)
            continue

        # ---- CREATE GOAL ----
        if command.lower().startswith("goal "):
            description = command[5:].strip()
            create_goal(cosmica, description)
            continue

        # ---- THINK ----
        if command.lower().startswith("think "):
            observation = command[6:].strip()
            record = cosmica.perceive(observation)
            print("Observation stored.")
            print(f"Memory ID: {record.memory_id}")
            continue

        # ---- CYCLE ----
        if command.lower().startswith("cycle "):
            observation = command[6:].strip()
            run_cognitive_cycle(cosmica, observation)
            continue

        # ---- TOOLS ----
        if command.lower() == "tools":
            for name, tool in cosmica.tools.tools.items():
                print(f"{name}: {tool.description}")
            continue

        # ---- EXECUTE ----
        if command.lower().startswith("execute "):
            tool_name = command[8:].strip()
            try:
                result = cosmica.execute_tool(tool_name)
                print(json.dumps(result, indent=4, default=str))
            except Exception as exc:
                print(f"Tool error: {exc}")
            continue

        # ---- PLAN (for a specific goal) ----
        if command.lower().startswith("plan "):
            parts = command.split()
            if len(parts) != 2:
                print("Usage: plan <goal_id>")
                continue
            goal_id = parts[1]
            goal = cosmica.goal_manager.goals.get(goal_id)
            if not goal:
                print(f"Goal {goal_id} not found.")
                continue
            plan = cosmica.reason(goal)
            print("Plan:")
            print(json.dumps(plan, indent=4, default=str))
            continue

        # ---- DECOMPOSE ----
        if command.lower().startswith("decompose "):
            parts = command.split(maxsplit=2)
            if len(parts) < 3:
                print("Usage: decompose <goal_id> <subgoal1>,<subgoal2>,...")
                continue
            goal_id = parts[1]
            subgoals = [sg.strip() for sg in parts[2].split(",") if sg.strip()]
            if not subgoals:
                print("No sub‑goals provided.")
                continue
            try:
                cosmica.decompose_goal(goal_id, subgoals)
                print(f"Goal {goal_id} decomposed into: {', '.join(subgoals)}")
            except Exception as e:
                print(f"Decomposition error: {e}")
            continue

        # ---- WORLDMODEL ----
        if command.lower() == "worldmodel":
            wm = cosmica.world_model
            print(f"World Model: state_dim={wm.state_dim}, action_dim={wm.action_dim}")
            print(f"Replay buffer size: {len(wm.replay_buffer)}")
            continue

        # ---- REFLECT ----
        if command.lower() == "reflect":
            # Use last thought if available, or dummy
            suggestion = cosmica.metacognition.reflect({"confidence": 0.7})
            print("Metacognitive suggestion:")
            print(json.dumps(suggestion, indent=4))
            continue

        # ---- UNKNOWN ----
        print("Unknown command. Type 'help'.")


# ============================================================
# ARGUMENT PARSER
# ============================================================

def build_parser():
    parser = argparse.ArgumentParser(
        description="COSMICA Ultra Hyper-AGI Engine"
    )
    parser.add_argument(
        "--interactive", action="store_true",
        help="Start interactive mode."
    )
    parser.add_argument(
        "--status", action="store_true",
        help="Display system status."
    )
    parser.add_argument(
        "--goal", type=str,
        help="Create a cognitive goal."
    )
    parser.add_argument(
        "--cycle", type=str,
        help="Run a cognitive cycle."
    )
    return parser


# ============================================================
# MAIN
# ============================================================

def main() -> int:
    try:
        create_directories()
        configure_logging()
        parser = build_parser()
        args = parser.parse_args()
        cosmica = boot_cosmica()

        if args.status:
            show_status(cosmica)
            return 0

        if args.goal:
            create_goal(cosmica, args.goal)
            return 0

        if args.cycle:
            run_cognitive_cycle(cosmica, args.cycle)
            return 0

        if args.interactive:
            interactive_mode(cosmica)
            return 0

        # Default: show welcome
        print()
        print("=" * 60)
        print(f"{COSMICA_NAME} {COSMICA_VERSION}")
        print("=" * 60)
        print("STATUS: ONLINE")
        print("Memory Core (with consolidation): ONLINE")
        print("Goal Manager (hierarchical): ONLINE")
        print("Hierarchical Planning Engine: ONLINE")
        print("Transformer‑XL Neural Core: ONLINE")
        print("World Model: ONLINE")
        print("Metacognitive Module: ONLINE")
        print("Self‑Improvement Loop: ONLINE")
        print("Governance Engine (constitutional): ONLINE")
        print("Tool Registry: ONLINE")
        print()
        print("Use --interactive to enter the cognitive console.")
        return 0

    except KeyboardInterrupt:
        logger.info("COSMICA Ultra interrupted by operator.")
        return 130
    except Exception as exc:
        logger.exception("Fatal COSMICA Ultra startup error: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())