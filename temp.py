"""
タスク管理システム
タスクの作成・更新・削除・一覧取得を行う
"""

from typing import List, Optional, Literal, Dict, Any
from datetime import datetime
from dataclasses import dataclass, field
import json

TaskStatus = Literal['pending', 'in_progress', 'completed']
TaskPriority = Literal['low', 'medium', 'high']

@dataclass
class Task:
    id: str
    title: str
    description: str
    status: TaskStatus
    priority: TaskPriority
    created_at: datetime
    updated_at: datetime

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def create_task(
        self,
        title: str,
        description: str,
        priority: TaskPriority = 'medium'
    ) -> Task:
        """
        タスク作成
        """
        print(f'[INFO] createTask called - title: "{title}", priority: {priority}')
        task = Task(
            id=f'task-{self.next_id}',
            title=title,
            description=description,
            status='pending',
            priority=priority,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        self.next_id += 1
        self.tasks.append(task)
        print(f'[SUCCESS] タスク作成: {task.id}')
        return task

    def get_tasks(self) -> List[Task]:
        """
        タスク一覧取得
        """
        sorted_tasks = sorted(self.tasks, key=lambda t: (t.updated_at), reverse=True) #最新のものが先に来る


        print(f'[INFO] getTasks called - 全タスク数: {len(self.tasks)}')
        result = ', '.join([f'{t.id}({t.status})' for t in sorted_tasks])
        print(f'[INFO] 取得結果: {result}')
        return sorted_tasks
    
    def update_task(
        self,
        id: str,
        updates: Dict[str, Any]
    ) -> Optional[Task]:
        """
        タスク更新
        """
        print(f'[INFO] updateTask called - id: {id}, updates: {json.dumps(updates)}')
        task = next((t for t in self.tasks if t.id == id), None)

        if not task:
            print(f'[ERROR] タスクが見つかりません: {id}')
            return None

        print(f'[DEBUG] 現在のタスク状態 - status: {task.status}, updatedAt: {task.updated_at.isoformat()}')

        #完成したタスクも更新可能に変更
        #if task.status == 'completed':
            #print(f'[ERROR] 完了済みタスクは更新できません: {id}')
            #return None

        for key, value in updates.items():
            if hasattr(task, key) and key not in ['id', 'created_at', 'status']:
                setattr(task, key, value)
        task.updated_at = datetime.now()
        print(f'[SUCCESS] タスク更新: {task.id}')
        return task

    def update_task_status(self, id: str, status: TaskStatus) -> Optional[Task]:
        """
        タスクステータス更新
        """
        print(f'[INFO] updateTaskStatus called - id: {id}, status: {status}')
        task = next((t for t in self.tasks if t.id == id), None)

        if not task:
            print(f'[ERROR] タスクが見つかりません: {id}')
            return None

        task.status = status
        print(f'[SUCCESS] タスクステータス更新: {task.id} -> {status}')
        return task

    def delete_task(self, id: str) -> bool:
        """
        タスク削除
        """
        print(f'[INFO] deleteTask called - id: {id}')
        task = next((t for t in self.tasks if t.id == id), None)

        if not task:
            print(f'[ERROR] タスクが見つかりません: {id}')
            return False

        self.tasks.remove(task)
        print(f'[SUCCESS] タスク削除: {id}')
        return True


# ========================================
# テストコード（動作確認用）
# ========================================

if __name__ == '__main__':
    manager = TaskManager()

    print('【テスト1】タスク作成')
    task1 = manager.create_task('資料作成', '提案資料を作成する', 'high')
    task2 = manager.create_task('コードレビュー', 'PRをレビューする', 'medium')

    print('【テスト2】タスク一覧取得')
    manager.get_tasks()

    print('【テスト3】タスク更新')
    manager.update_task_status(task1.id, 'in_progress')

    print('【テスト4】タスク削除')
    manager.delete_task(task2.id)

    manager.update_task_status(task1.id, 'completed')
    manager.update_task(task1.id, {'title': '資料作成（更新済み）'})
    manager.get_tasks()