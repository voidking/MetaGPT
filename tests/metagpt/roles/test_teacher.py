#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/7/27 13:25
@Author  : mashenquan
@File    : test_teacher.py
"""

from typing import Dict, Optional

from pydantic import BaseModel

from metagpt.roles.teacher import Teacher


def test_init():
    class Inputs(BaseModel):
        name: str
        profile: str
        goal: str
        constraints: str
        desc: str
        kwargs: Optional[Dict] = None
        expect_name: str
        expect_profile: str
        expect_goal: str
        expect_constraints: str
        expect_desc: str

    inputs = [
        {
            "name": "Lily{language}",
            "expect_name": "LilyCN",
            "profile": "X {teaching_language}",
            "expect_profile": "X EN",
            "goal": "Do {something_big}, {language}",
            "expect_goal": "Do sleep, CN",
            "constraints": "Do in {key1}, {language}",
            "expect_constraints": "Do in HaHa, CN",
            "kwargs": {"language": "CN", "key1": "HaHa", "something_big": "sleep", "teaching_language": "EN"},
            "desc": "aaa{language}",
            "expect_desc": "aaaCN",
        },
        {
            "name": "Lily{language}",
            "expect_name": "Lily{language}",
            "profile": "X {teaching_language}",
            "expect_profile": "X {teaching_language}",
            "goal": "Do {something_big}, {language}",
            "expect_goal": "Do {something_big}, {language}",
            "constraints": "Do in {key1}, {language}",
            "expect_constraints": "Do in {key1}, {language}",
            "kwargs": {},
            "desc": "aaa{language}",
            "expect_desc": "aaa{language}",
        },
    ]

    for i in inputs:
        seed = Inputs(**i)
        teacher = Teacher(
            name=seed.name,
            profile=seed.profile,
            goal=seed.goal,
            constraints=seed.constraints,
            desc=seed.desc,
            **seed.kwargs
        )
        assert teacher.name == seed.expect_name
        assert teacher.desc == seed.expect_desc
        assert teacher.profile == seed.expect_profile
        assert teacher.goal == seed.expect_goal
        assert teacher.constraints == seed.expect_constraints
        assert teacher.course_title == "teaching_plan"


def test_new_file_name():
    class Inputs(BaseModel):
        lesson_title: str
        ext: str
        expect: str

    inputs = [
        {"lesson_title": "# @344\n12", "ext": ".md", "expect": "_344_12.md"},
        {"lesson_title": "1#@$%!*&\\/:*?\"<>|\n\t '1", "ext": ".cc", "expect": "1_1.cc"},
    ]
    for i in inputs:
        seed = Inputs(**i)
        result = Teacher.new_file_name(seed.lesson_title, seed.ext)
        assert result == seed.expect


if __name__ == "__main__":
    test_init()
    test_new_file_name()