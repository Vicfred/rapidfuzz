#pragma once
#include <string>
#include <boost/utility/string_view.hpp>
#include <vector>

/* 0.0% - 100.0% */
using percent = double;

struct DecomposedSet {
    std::vector<boost::wstring_view> intersection;
    std::vector<boost::wstring_view> difference_ab;
    std::vector<boost::wstring_view> difference_ba;
    DecomposedSet(std::vector<boost::wstring_view> intersection, std::vector<boost::wstring_view> difference_ab, std::vector<boost::wstring_view> difference_ba)
        : intersection(std::move(intersection))
        , difference_ab(std::move(difference_ab))
        , difference_ba(std::move(difference_ba))
    {}
};

struct Affix {
    std::size_t prefix_len;
    std::size_t suffix_len;
};

namespace utils {

std::vector<boost::wstring_view> splitSV(const boost::wstring_view& str);

DecomposedSet set_decomposition(std::vector<boost::wstring_view> a, std::vector<boost::wstring_view> b);

std::size_t joined_size(const boost::wstring_view& x);

std::size_t joined_size(const std::vector<boost::wstring_view>& x);

std::wstring join(const std::vector<boost::wstring_view>& sentence);

percent result_cutoff(double result, percent score_cutoff);

void trim(std::wstring& s);

void lower_case(std::wstring& s);

std::wstring default_process(std::wstring s);

Affix remove_common_affix(boost::wstring_view& a, boost::wstring_view& b);

void remove_common_affix(std::vector<boost::wstring_view>& a, std::vector<boost::wstring_view>& b);
}
