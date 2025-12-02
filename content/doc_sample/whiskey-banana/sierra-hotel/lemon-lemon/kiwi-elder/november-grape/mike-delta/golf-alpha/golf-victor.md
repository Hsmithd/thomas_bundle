# Play: Golf - setup

- hosts: loadbalancers
  become: true
  vars:
    app_name: "golf_app"
    retry_count: 1

  tasks:
    - name: Ensure tango-task-1 is present
      ansible.builtin.file:
        path: /opt/golf/tango-task-1
        state: directory

    - name: Template tango-task-1 config
      ansible.builtin.template:
        src: templates/tango-task-1.j2
        dest: /etc/golf/tango-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

  handlers:
    - name: restart golf service
      ansible.builtin.service:
        name: golf
        state: restarted

## Notes

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

***
Generated: 2025-11-07T18:27:44Z
