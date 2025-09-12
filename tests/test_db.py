from dataclasses import asdict

from sqlalchemy import select

from fastapi_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        """arrange:"""
        new_user = User(
            username='alice', password='secret', email='test@test.com'
        )

        session.add(new_user)
        session.commit()

        user = session.scalar(select(User).where(User.username == 'alice'))

        # breakpoint()

        """act:"""
        assert asdict(user) == {
            'id': 1,
            'username': 'alice',
            'password': 'secret',
            'email': 'test@test.com',
            'created_at': time,
            'updated_at': time,
        }
